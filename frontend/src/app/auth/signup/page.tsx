'use client'
import { useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { apiRegister, extractToken } from '@/lib/api'
import { setToken } from '@/lib/auth'

export default function SignUpPage() {
  const router = useRouter()
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError(null)
    setLoading(true)
    try {
      const data = await apiRegister(name, email, password)
      const token = extractToken(data)
      if (!token) throw new Error('No token in response')
      setToken(token)
      router.replace('/dashboard')
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : 'Registration failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-[#0F1117] flex items-center justify-center p-4">
      <div className="w-full max-w-sm">
        <div className="mb-8 text-center">
          <span className="font-mono text-xs tracking-widest text-[#4F9CF9] uppercase">MedBilling</span>
          <h1 className="text-2xl font-semibold text-[#E8EAF0] mt-2">Create account</h1>
        </div>

        <form
          onSubmit={handleSubmit}
          className="bg-[#1A1D27] border border-[#2A2D3A] rounded-lg p-6 space-y-4"
        >
          {error && (
            <div className="text-sm text-[#EF4444] bg-[#EF4444]/10 border border-[#EF4444]/20 rounded px-3 py-2">
              {error}
            </div>
          )}

          <div className="space-y-1">
            <label htmlFor="name" className="block text-xs font-mono text-[#6B7280] uppercase tracking-wider">
              Name
            </label>
            <input
              id="name"
              type="text"
              required
              value={name}
              onChange={e => setName(e.target.value)}
              placeholder="Jane Smith"
              className="w-full bg-[#0F1117] border border-[#2A2D3A] rounded px-3 py-2 text-[#E8EAF0] text-sm focus:outline-none focus:border-[#4F9CF9] transition-colors"
            />
          </div>

          <div className="space-y-1">
            <label htmlFor="email" className="block text-xs font-mono text-[#6B7280] uppercase tracking-wider">
              Email
            </label>
            <input
              id="email"
              type="email"
              required
              value={email}
              onChange={e => setEmail(e.target.value)}
              placeholder="jane@example.com"
              className="w-full bg-[#0F1117] border border-[#2A2D3A] rounded px-3 py-2 text-[#E8EAF0] text-sm focus:outline-none focus:border-[#4F9CF9] transition-colors"
            />
          </div>

          <div className="space-y-1">
            <label htmlFor="password" className="block text-xs font-mono text-[#6B7280] uppercase tracking-wider">
              Password
            </label>
            <input
              id="password"
              type="password"
              required
              value={password}
              onChange={e => setPassword(e.target.value)}
              placeholder="••••••••"
              className="w-full bg-[#0F1117] border border-[#2A2D3A] rounded px-3 py-2 text-[#E8EAF0] text-sm focus:outline-none focus:border-[#4F9CF9] transition-colors"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-[#4F9CF9] text-white rounded py-2 text-sm font-medium hover:bg-[#3B8EE8] transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? 'Creating account…' : 'Create account'}
          </button>
        </form>

        <p className="text-center text-sm text-[#6B7280] mt-4">
          Already have an account?{' '}
          <Link href="/auth/signin" className="text-[#4F9CF9] hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </main>
  )
}
