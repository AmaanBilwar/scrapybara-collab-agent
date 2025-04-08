import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import { Home, Clipboard, InfoIcon } from "lucide-react";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Scrapybara Collab Agent",
  description: "A multi-agent collaborative system for web research",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <nav className="flex items-center justify-between px-6 py-4 border-b">
          <div className="flex items-center space-x-2">
            <span className="font-bold text-xl">Scrapybara</span>
          </div>
          <div className="flex items-center space-x-6">
            <Link 
              href="/" 
              className="flex items-center space-x-1 hover:text-blue-600 transition-colors"
            >
              <Home size={18} />
              <span>Home</span>
            </Link>
            <Link 
              href="/research" 
              className="flex items-center space-x-1 hover:text-blue-600 transition-colors"
            >
              <Clipboard size={18} />
              <span>Use The App</span>
            </Link>
            <Link 
              href="/about" 
              className="flex items-center space-x-1 hover:text-blue-600 transition-colors"
            >
              <InfoIcon size={18} />
              <span>About</span>
            </Link>
          </div>
        </nav>
        <main>{children}</main>
      </body>
    </html>
  );
}
