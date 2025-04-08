'use client';

import { useState } from 'react';
import Link from 'next/link';
import { Bot, BookOpen, Cpu, FileText, DownloadCloud, ArrowRight, Database, Globe } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';

export default function Page() {
  return (
    <div className="container mx-auto px-4 py-8">
      {/* Hero Section */}
      <section className="py-12 md:py-24 flex flex-col items-center text-center">
        <div className="mx-auto max-w-3xl">
          <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">
            Scrapybara Collaborative Agents Framework
          </h1>
          <p className="mt-6 text-xl text-gray-600">
            A multi-agent collaborative system for intelligent web research and note-taking
          </p>
          <div className="mt-8 flex flex-wrap justify-center gap-4">
            <Button asChild size="lg">
              <Link href="/research">
                Get Started <ArrowRight className="ml-2 h-4 w-4" />
              </Link>
            </Button>
            <Button variant="outline" size="lg" asChild>
              <a href="https://github.com/AmaanBilwar/scrapybara-collab-agent" target="_blank" rel="noopener noreferrer">
                View on GitHub
              </a>
            </Button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-12">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold">How It Works</h2>
          <p className="text-gray-600 mt-4">
            Our framework demonstrates how two AI agents collaborate toward a common goal
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <Card>
            <CardHeader>
              <Bot className="h-8 w-8 mb-2 text-blue-600" />
              <CardTitle>Research Agent</CardTitle>
              <CardDescription>
                Web browsing specialist
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p>
                Uses Scrapybara's cloud browsers to gather information on specified topics.
                Searches websites, extracts relevant content, and takes screenshots as evidence.
              </p>
            </CardContent>
          </Card>
          
          <Card>
            <CardHeader>
              <FileText className="h-8 w-8 mb-2 text-green-600" />
              <CardTitle>Notes Agent</CardTitle>
              <CardDescription>
                Content processing specialist
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p>
                Processes the research, formats the content into structured notes, 
                and saves everything to a text file. Creates summaries of all research topics.
              </p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Process Section */}
      <section className="py-12">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold">The Collaboration Process</h2>
          <p className="text-gray-600 mt-4">
            Agents communicate through a shared memory system
          </p>
        </div>
        
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          <Card>
            <CardHeader className="flex flex-col items-center">
              <div className="bg-blue-100 p-3 rounded-full">
                <Database className="h-6 w-6 text-blue-600" />
              </div>
              <CardTitle className="text-center mt-4">Shared Memory</CardTitle>
            </CardHeader>
            <CardContent className="text-center">
              <p>Provides a key-value store that allows agents to share data</p>
            </CardContent>
          </Card>
          
          <Card>
            <CardHeader className="flex flex-col items-center">
              <div className="bg-green-100 p-3 rounded-full">
                <Globe className="h-6 w-6 text-green-600" />
              </div>
              <CardTitle className="text-center mt-4">Web Research</CardTitle>
            </CardHeader>
            <CardContent className="text-center">
              <p>Research Agent searches for information on specified topics</p>
            </CardContent>
          </Card>
          
          <Card>
            <CardHeader className="flex flex-col items-center">
              <div className="bg-purple-100 p-3 rounded-full">
                <BookOpen className="h-6 w-6 text-purple-600" />
              </div>
              <CardTitle className="text-center mt-4">Content Processing</CardTitle>
            </CardHeader>
            <CardContent className="text-center">
              <p>Notes Agent formats and structures the research data</p>
            </CardContent>
          </Card>
          
          <Card>
            <CardHeader className="flex flex-col items-center">
              <div className="bg-orange-100 p-3 rounded-full">
                <DownloadCloud className="h-6 w-6 text-orange-600" />
              </div>
              <CardTitle className="text-center mt-4">Output Generation</CardTitle>
            </CardHeader>
            <CardContent className="text-center">
              <p>Research notes are compiled and saved to a text file</p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-12 md:py-24 text-center">
        <div className="mx-auto max-w-3xl">
          <h2 className="text-3xl font-bold">Ready to Start Researching?</h2>
          <p className="mt-4 text-xl text-gray-600">
            Try our collaborative agent system for efficient web research and note-taking
          </p>
          <div className="mt-8">
            <Button size="lg" asChild>
              <Link href="/research">Use The App</Link>
            </Button>
          </div>
        </div>
      </section>
    </div>
  );
}