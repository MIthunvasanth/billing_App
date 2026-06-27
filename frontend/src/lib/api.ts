import { getToken, clearToken } from './auth'

const BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000'

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message)
    this.name = 'ApiError'
  }
}

interface SuccessEnvelope<T> {
  success: boolean
  message: string
  data: T
}

async function apiFetch<T>(path: string, options: RequestInit = {}): Promise<T> {
  const token = getToken()
  const headers: Record<string, string> = { ...(options.headers as Record<string, string> ?? {}) }

  if (token) headers['Authorization'] = `Bearer ${token}`
  // Do not set Content-Type for FormData — browser sets it with boundary
  if (options.body && !(options.body instanceof FormData)) {
    headers['Content-Type'] = 'application/json'
  }

  const res = await fetch(`${BASE}${path}`, { ...options, headers })

  if (res.status === 401) {
    clearToken()
    if (typeof window !== 'undefined') window.location.href = '/auth/signin'
    throw new ApiError(401, 'Unauthorized')
  }

  if (!res.ok) {
    let msg = res.statusText
    try { msg = await res.text() } catch { /* ignore */ }
    throw new ApiError(res.status, msg)
  }

  if (res.status === 204) return undefined as T

  const json = await res.json()

  // Unwrap SuccessResponse envelope: { success, message, data } → data
  if (json !== null && typeof json === 'object' && 'data' in json && 'success' in json) {
    return (json as SuccessEnvelope<T>).data
  }
  return json as T
}

// ---------------------------------------------------------------------------
// Auth
// ---------------------------------------------------------------------------

export interface AuthResponse {
  token?: string
  user?: { token?: string; id?: string; email?: string; name?: string }
}

export async function apiRegister(name: string, email: string, password: string): Promise<AuthResponse> {
  return apiFetch<AuthResponse>('/auth/register', {
    method: 'POST',
    body: JSON.stringify({ name, email, password }),
  })
}

export async function apiLogin(email: string, password: string): Promise<AuthResponse> {
  return apiFetch<AuthResponse>('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  })
}

export function extractToken(data: AuthResponse): string | null {
  return data.token ?? data.user?.token ?? null
}

// ---------------------------------------------------------------------------
// Jobs
// ---------------------------------------------------------------------------

export interface TokenUsage {
  input: number
  output: number
  total: number
}

export interface BillingRecord {
  treatment_date: string
  cpt_codes: string[]
  description: string | null
  provider: string
  insurers: string[]
  third_parties: string[]
  total_charges: number | null
  ins_paid: number | null
  adjustment: number | null
  payments: number | null
  balance: number | null
  page: string
}

export interface FlaggedRecord {
  row: number | null
  fields: string[]
  reason: string
  page: string
  severity: 'low' | 'medium' | 'high'
}

export interface ExtractionResult {
  records: BillingRecord[]
  flagged: FlaggedRecord[]
}

export interface Job {
  // Backend uses 'id' as primary key field
  id: string
  job_id?: string  // alias some responses may include
  status: 'pending' | 'processing' | 'completed' | 'failed' | 'cancelled'
  pdf_filename?: string
  pdf_path?: string
  created_at: string
  updated_at?: string
  // Python Decimal serializes as string; accept string | number
  processing_duration_seconds: number | string | null
  token_usage: TokenUsage | null
  cost_usd: number | string | null
  result?: ExtractionResult | null
  error?: string | null
}

export function jobId(job: Job): string {
  return job.id ?? job.job_id ?? ''
}

/** Parse Decimal/string to number, null if absent */
export function toNum(v: number | string | null | undefined): number | null {
  if (v == null) return null
  const n = typeof v === 'number' ? v : parseFloat(String(v))
  return isNaN(n) ? null : n
}

export async function apiUploadJob(file: File): Promise<Job> {
  const form = new FormData()
  form.append('file', file)
  return apiFetch<Job>('/jobs', { method: 'POST', body: form })
}

export async function apiListJobs(status?: string): Promise<Job[]> {
  const qs = status ? `?status=${encodeURIComponent(status)}` : ''
  const data = await apiFetch<Job[] | unknown>(`/jobs${qs}`)
  return Array.isArray(data) ? data as Job[] : []
}

export async function apiGetJob(id: string): Promise<Job> {
  return apiFetch<Job>(`/jobs/${encodeURIComponent(id)}`)
}

export async function apiCancelJob(id: string): Promise<Job> {
  return apiFetch<Job>(`/jobs/${encodeURIComponent(id)}`, { method: 'DELETE' })
}
