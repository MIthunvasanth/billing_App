import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'MedBilling',
  description: 'AI-powered medical billing record extraction',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
