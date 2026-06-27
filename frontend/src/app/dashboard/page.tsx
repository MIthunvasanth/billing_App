'use client'
import { useState, useEffect, useRef, useCallback } from 'react'
import { useRouter } from 'next/navigation'
import { getToken, clearToken } from '@/lib/auth'
import { apiUploadJob, apiListJobs, Job, jobId, toNum, ApiError } from '@/lib/api'

const STATUS_BADGE: Record<string, string> = {
  pending:    'text-[#9CA3AF] bg-[#9CA3AF]/10 border-[#9CA3AF]/20',
  processing: 'text-[#F59E0B] bg-[#F59E0B]/10 border-[#F59E0B]/20',
  completed:  'text-[#10B981] bg-[#10B981]/10 border-[#10B981]/20',
  failed:     'text-[#EF4444] bg-[#EF4444]/10 border-[#EF4444]/20',
  cancelled:  'text-[#6B7280] bg-[#6B7280]/10 border-[#6B7280]/20',
}

function StatusBadge({ status }: { status: string }) {
  return (
    <span className={`font-mono text-xs px-2 py-0.5 rounded border ${STATUS_BADGE[status] ?? STATUS_BADGE.pending}`}>
      {status}
    </span>
  )
}

function fmtDate(iso: string) {
  return new Date(iso).toLocaleString(undefined, { dateStyle: 'short', timeStyle: 'short' })
}

function truncId(id: string) {
  return id.length > 8 ? id.slice(0, 8) + '…' : id
}

export default function DashboardPage() {
  const router = useRouter()
  const [ready, setReady] = useState(false)
  const [jobs, setJobs] = useState<Job[]>([])
  const [jobsLoading, setJobsLoading] = useState(true)
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [uploading, setUploading] = useState(false)
  const [uploadError, setUploadError] = useState<string | null>(null)
  const fileRef = useRef<HTMLInputElement>(null)
  const pollRef = useRef<ReturnType<typeof setInterval> | null>(null)

  // Auth guard
  useEffect(() => {
    if (!getToken()) {
      router.replace('/auth/signin')
      return
    }
    setReady(true)
  }, [router])

  const fetchJobs = useCallback(async () => {
    try {
      const list = await apiListJobs()
      setJobs(list)
    } catch (err) {
      if (err instanceof ApiError && err.status === 401) return // apiFetch redirects
    } finally {
      setJobsLoading(false)
    }
  }, [])

  useEffect(() => {
    if (!ready) return
    fetchJobs()
    pollRef.current = setInterval(fetchJobs, 5000)
    return () => {
      if (pollRef.current) clearInterval(pollRef.current)
    }
  }, [ready, fetchJobs])

  async function handleUpload() {
    if (!selectedFile) return
    setUploadError(null)
    setUploading(true)
    try {
      const job = await apiUploadJob(selectedFile)
      setJobs(prev => [job, ...prev])
      setSelectedFile(null)
      if (fileRef.current) fileRef.current.value = ''
    } catch (err: unknown) {
      setUploadError(err instanceof Error ? err.message : 'Upload failed')
    } finally {
      setUploading(false)
    }
  }

  function handleSignOut() {
    clearToken()
    router.replace('/auth/signin')
  }

  if (!ready) return null

  return (
    <div className="min-h-screen bg-[#0F1117] text-[#E8EAF0]">
      {/* Header */}
      <header className="border-b border-[#2A2D3A] px-6 py-4 flex items-center justify-between">
        <span className="font-mono text-xs tracking-widest text-[#4F9CF9] uppercase">MedBilling</span>
        <button
          onClick={handleSignOut}
          className="font-mono text-xs text-[#6B7280] hover:text-[#E8EAF0] transition-colors"
        >
          Sign out
        </button>
      </header>

      <main className="max-w-5xl mx-auto px-6 py-8 space-y-10">
        {/* Upload section */}
        <section>
          <h2 className="font-mono text-xs uppercase tracking-widest text-[#6B7280] mb-3">Upload PDF</h2>
          <div className="bg-[#1A1D27] border border-[#2A2D3A] rounded-lg p-5">
            {uploadError && (
              <div className="mb-4 text-sm text-[#EF4444] bg-[#EF4444]/10 border border-[#EF4444]/20 rounded px-3 py-2">
                {uploadError}
              </div>
            )}
            <div className="flex items-center gap-4 flex-wrap">
              <div className="flex-1 min-w-0">
                <input
                  ref={fileRef}
                  type="file"
                  accept=".pdf"
                  onChange={e => setSelectedFile(e.target.files?.[0] ?? null)}
                  className="block w-full text-sm text-[#6B7280]
                    file:mr-3 file:py-1.5 file:px-3 file:rounded
                    file:border file:border-[#2A2D3A] file:text-xs file:font-mono
                    file:bg-[#0F1117] file:text-[#E8EAF0]
                    hover:file:border-[#4F9CF9] file:transition-colors file:cursor-pointer"
                />
                {selectedFile && (
                  <p className="mt-1 text-xs font-mono text-[#6B7280]">
                    {selectedFile.name} ({(selectedFile.size / 1024).toFixed(1)} KB)
                  </p>
                )}
              </div>
              <button
                onClick={handleUpload}
                disabled={!selectedFile || uploading}
                className="px-4 py-2 bg-[#4F9CF9] text-white text-sm font-mono rounded hover:bg-[#3B8EE8] transition-colors disabled:opacity-50 disabled:cursor-not-allowed whitespace-nowrap"
              >
                {uploading ? 'Uploading…' : 'Upload'}
              </button>
            </div>
          </div>
        </section>

        {/* Job list */}
        <section>
          <h2 className="font-mono text-xs uppercase tracking-widest text-[#6B7280] mb-3">
            Jobs{jobs.length > 0 && <span className="text-[#4F9CF9] ml-1">({jobs.length})</span>}
          </h2>
          <div className="bg-[#1A1D27] border border-[#2A2D3A] rounded-lg overflow-hidden">
            {jobsLoading ? (
              <p className="px-6 py-10 text-center text-sm font-mono text-[#6B7280]">Loading…</p>
            ) : jobs.length === 0 ? (
              <p className="px-6 py-10 text-center text-sm text-[#6B7280]">
                No jobs yet. Upload a PDF to get started.
              </p>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b border-[#2A2D3A]">
                      {['Job ID', 'File', 'Status', 'Created', 'Duration'].map(h => (
                        <th key={h} className="px-4 py-3 text-left text-xs font-mono text-[#6B7280] uppercase tracking-wider whitespace-nowrap">
                          {h}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {jobs.map((job, i) => (
                      <tr
                        key={jobId(job)}
                        onClick={() => router.push(`/jobs/${jobId(job)}`)}
                        className={`cursor-pointer hover:bg-[#0F1117] transition-colors ${i < jobs.length - 1 ? 'border-b border-[#2A2D3A]' : ''}`}
                      >
                        <td className="px-4 py-3 font-mono text-xs text-[#4F9CF9] whitespace-nowrap">
                          {truncId(jobId(job))}
                        </td>
                        <td className="px-4 py-3 text-xs text-[#E8EAF0] max-w-[180px] truncate">
                          {job.pdf_filename ?? '—'}
                        </td>
                        <td className="px-4 py-3">
                          <StatusBadge status={job.status} />
                        </td>
                        <td className="px-4 py-3 text-xs font-mono text-[#6B7280] whitespace-nowrap">
                          {job.created_at ? fmtDate(job.created_at) : '—'}
                        </td>
                        <td className="px-4 py-3 text-xs font-mono text-[#6B7280] whitespace-nowrap">
                          {toNum(job.processing_duration_seconds) != null
                            ? `${toNum(job.processing_duration_seconds)!.toFixed(1)}s`
                            : '—'}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </section>
      </main>
    </div>
  )
}
