'use client'
import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { getToken } from '@/lib/auth'
import { apiGetJob, Job, BillingRecord, FlaggedRecord, jobId, toNum, ApiError } from '@/lib/api'

// ---------------------------------------------------------------------------
// Design tokens
// ---------------------------------------------------------------------------

const STATUS_COLOR: Record<string, string> = {
  pending:    'text-[#9CA3AF]',
  processing: 'text-[#F59E0B]',
  completed:  'text-[#10B981]',
  failed:     'text-[#EF4444]',
  cancelled:  'text-[#6B7280]',
}

const SEVERITY_STYLE: Record<string, string> = {
  low:    'border-[#EAB308]/30 bg-[#EAB308]/5',
  medium: 'border-[#F97316]/30 bg-[#F97316]/5',
  high:   'border-[#EF4444]/30 bg-[#EF4444]/5',
}

const SEVERITY_TEXT: Record<string, string> = {
  low:    'text-[#EAB308]',
  medium: 'text-[#F97316]',
  high:   'text-[#EF4444]',
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function fmtMoney(n: number | null | undefined) {
  if (n == null) return <span className="text-[#6B7280]">—</span>
  return <span>${n.toFixed(2)}</span>
}

function fmtNum(n: number | null | undefined) {
  if (n == null) return '—'
  return n.toLocaleString()
}

// ---------------------------------------------------------------------------
// Sub-components
// ---------------------------------------------------------------------------

function MetricBox({ label, value }: { label: string; value: React.ReactNode }) {
  return (
    <div>
      <p className="text-xs font-mono text-[#6B7280] uppercase tracking-wider mb-1">{label}</p>
      <p className="font-mono text-sm text-[#E8EAF0]">{value}</p>
    </div>
  )
}

function BillingTable({ records }: { records: BillingRecord[] }) {
  const cols: { key: keyof BillingRecord; label: string; mono?: boolean; right?: boolean }[] = [
    { key: 'treatment_date', label: 'Date',      mono: true },
    { key: 'cpt_codes',      label: 'CPT',       mono: true },
    { key: 'description',    label: 'Description' },
    { key: 'provider',       label: 'Provider' },
    { key: 'total_charges',  label: 'Total',     mono: true, right: true },
    { key: 'ins_paid',       label: 'Ins Paid',  mono: true, right: true },
    { key: 'adjustment',     label: 'Adj',       mono: true, right: true },
    { key: 'payments',       label: 'Payments',  mono: true, right: true },
    { key: 'balance',        label: 'Balance',   mono: true, right: true },
    { key: 'page',           label: 'Page',      mono: true },
  ]

  function renderCell(rec: BillingRecord, key: keyof BillingRecord, right?: boolean) {
    const v = rec[key]
    if (v == null) return <span className="text-[#6B7280]">—</span>
    if (Array.isArray(v)) {
      return <span className="text-[#4F9CF9]">{v.join(', ') || '—'}</span>
    }
    if (typeof v === 'number') {
      const colored = key === 'ins_paid'  ? 'text-[#10B981]'
                    : key === 'balance'   ? 'text-[#F59E0B]'
                    : 'text-[#E8EAF0]'
      return <span className={colored}>${v.toFixed(2)}</span>
    }
    return <span>{String(v)}</span>
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-xs font-mono whitespace-nowrap">
        <thead>
          <tr className="border-b border-[#2A2D3A]">
            {cols.map(c => (
              <th
                key={c.key}
                className={`px-3 py-2 text-[#6B7280] uppercase tracking-wider font-mono ${c.right ? 'text-right' : 'text-left'}`}
              >
                {c.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {records.map((rec, i) => (
            <tr
              key={i}
              className={`hover:bg-[#0F1117] transition-colors ${i < records.length - 1 ? 'border-b border-[#2A2D3A]' : ''}`}
            >
              {cols.map(c => (
                <td
                  key={c.key}
                  className={`px-3 py-2 ${c.right ? 'text-right' : ''} ${c.key === 'description' ? 'max-w-[180px] truncate' : ''}`}
                >
                  {renderCell(rec, c.key, c.right)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

function FlaggedList({ flagged }: { flagged: FlaggedRecord[] }) {
  return (
    <div className="space-y-2">
      {flagged.map((f, i) => (
        <div
          key={i}
          className={`border rounded-lg px-4 py-3 ${SEVERITY_STYLE[f.severity] ?? SEVERITY_STYLE.low}`}
        >
          <div className="flex items-center gap-3 mb-1 flex-wrap">
            <span className={`font-mono text-xs font-bold uppercase ${SEVERITY_TEXT[f.severity] ?? ''}`}>
              {f.severity}
            </span>
            {f.row != null && (
              <span className="font-mono text-xs text-[#6B7280]">row {f.row}</span>
            )}
            {f.fields.length > 0 && (
              <span className="font-mono text-xs text-[#E8EAF0]">{f.fields.join(', ')}</span>
            )}
            <span className="font-mono text-xs text-[#6B7280] ml-auto">p.{f.page}</span>
          </div>
          <p className="text-xs text-[#C0C4D0]">{f.reason}</p>
        </div>
      ))}
    </div>
  )
}

// ---------------------------------------------------------------------------
// Page
// ---------------------------------------------------------------------------

export default function JobDetailPage({ params }: { params: { id: string } }) {
  const router = useRouter()
  const id = params.id

  const [job, setJob] = useState<Job | null>(null)
  const [notFound, setNotFound] = useState(false)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!getToken()) {
      router.replace('/auth/signin')
      return
    }
    apiGetJob(id)
      .then(setJob)
      .catch(err => {
        if (err instanceof ApiError && err.status === 404) setNotFound(true)
      })
      .finally(() => setLoading(false))
  }, [id, router])

  // Poll while processing
  useEffect(() => {
    if (!job || job.status !== 'processing') return
    const t = setInterval(() => {
      apiGetJob(id).then(setJob).catch(() => {})
    }, 3000)
    return () => clearInterval(t)
  }, [job, id])

  if (loading) {
    return (
      <div className="min-h-screen bg-[#0F1117] flex items-center justify-center">
        <span className="font-mono text-sm text-[#6B7280]">Loading…</span>
      </div>
    )
  }

  if (notFound) {
    return (
      <div className="min-h-screen bg-[#0F1117] flex items-center justify-center">
        <div className="text-center space-y-4">
          <p className="font-mono text-sm text-[#EF4444]">Job not found.</p>
          <Link href="/dashboard" className="text-sm text-[#4F9CF9] hover:underline">
            ← Back to dashboard
          </Link>
        </div>
      </div>
    )
  }

  if (!job) return null

  const records = job.result?.records ?? []
  const flagged = job.result?.flagged ?? []

  return (
    <div className="min-h-screen bg-[#0F1117] text-[#E8EAF0]">
      {/* Header */}
      <header className="border-b border-[#2A2D3A] px-6 py-4 flex items-center gap-4">
        <Link href="/dashboard" className="font-mono text-xs text-[#4F9CF9] hover:underline">
          ← Dashboard
        </Link>
        <span className="text-[#2A2D3A]">|</span>
        <span className="font-mono text-xs tracking-widest text-[#4F9CF9] uppercase">MedBilling</span>
      </header>

      <main className="max-w-6xl mx-auto px-6 py-8 space-y-8">
        {/* Job metadata card */}
        <section className="bg-[#1A1D27] border border-[#2A2D3A] rounded-lg p-6">
          <div className="flex items-start justify-between mb-4">
            <div>
              <p className="font-mono text-xs text-[#6B7280] uppercase tracking-wider mb-1">Job ID</p>
              <p className="font-mono text-sm">{jobId(job)}</p>
            </div>
            <span className={`font-mono text-sm font-medium ${STATUS_COLOR[job.status] ?? ''}`}>
              ● {job.status}
            </span>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-[#2A2D3A]">
            <MetricBox
              label="Duration"
              value={toNum(job.processing_duration_seconds) != null
                ? `${toNum(job.processing_duration_seconds)!.toFixed(1)}s`
                : '—'}
            />
            <MetricBox
              label="Cost"
              value={toNum(job.cost_usd) != null ? `$${toNum(job.cost_usd)!.toFixed(4)}` : '—'}
            />
            <MetricBox
              label="Tokens in"
              value={fmtNum(job.token_usage?.input)}
            />
            <MetricBox
              label="Tokens out"
              value={fmtNum(job.token_usage?.output)}
            />
          </div>

          {job.error && (
            <div className="mt-4 text-sm text-[#EF4444] bg-[#EF4444]/10 border border-[#EF4444]/20 rounded px-3 py-2 font-mono">
              {job.error}
            </div>
          )}
        </section>

        {/* Billing records */}
        {records.length > 0 && (
          <section>
            <h2 className="font-mono text-xs uppercase tracking-widest text-[#6B7280] mb-3">
              Billing Records <span className="text-[#4F9CF9]">({records.length})</span>
            </h2>
            <div className="bg-[#1A1D27] border border-[#2A2D3A] rounded-lg overflow-hidden">
              <BillingTable records={records} />
            </div>
          </section>
        )}

        {/* Flagged records */}
        {flagged.length > 0 && (
          <section>
            <h2 className="font-mono text-xs uppercase tracking-widest text-[#6B7280] mb-3">
              Flagged <span className="text-[#F59E0B]">({flagged.length})</span>
            </h2>
            <FlaggedList flagged={flagged} />
          </section>
        )}

        {/* Completed but empty */}
        {job.status === 'completed' && records.length === 0 && flagged.length === 0 && (
          <p className="text-center py-12 text-sm text-[#6B7280]">
            Extraction complete — no billing records found.
          </p>
        )}

        {/* Still processing */}
        {job.status === 'processing' && (
          <p className="text-center py-12 text-sm font-mono text-[#F59E0B] animate-pulse">
            Processing… refreshing automatically
          </p>
        )}
      </main>
    </div>
  )
}
