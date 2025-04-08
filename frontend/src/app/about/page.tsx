import { CheckCircle } from 'lucide-react';

export default function AboutPage() {
  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-3xl font-bold mb-8">About Scrapybara Collaborative Agents</h1>
      
      <div className="prose max-w-none">
        <p className="text-lg">
          The Scrapybara Collaborative Agents Framework is a multi-agent system built to demonstrate 
          how different AI agents can work together on the same machine toward a common goal.
        </p>
        
        <h2 className="text-2xl font-bold mt-8 mb-4">Project Overview</h2>
        <p>
          This project creates a collaborative system with two specialized agents:
        </p>
        <ul className="space-y-2 my-4">
          <li className="flex items-start">
            <CheckCircle className="h-5 w-5 mr-2 text-green-500 flex-shrink-0 mt-0.5" />
            <span><strong>Research Agent:</strong> Browses the web using Scrapybara's cloud browsers to gather information on specified topics</span>
          </li>
          <li className="flex items-start">
            <CheckCircle className="h-5 w-5 mr-2 text-green-500 flex-shrink-0 mt-0.5" />
            <span><strong>Notes Agent:</strong> Processes the research, formats it, and saves it to a text file</span>
          </li>
        </ul>
        
        <p>
          The agents communicate through a shared memory system, allowing them to coordinate their activities effectively.
        </p>
        
        <h2 className="text-2xl font-bold mt-8 mb-4">How It Works</h2>
        
        <h3 className="text-xl font-semibold mt-6 mb-3">1. Shared Memory</h3>
        <p>
          The SharedMemory class provides a simple key-value store that allows agents to share data:
        </p>
        <ul className="list-disc ml-6 my-3">
          <li><code>save(key, value)</code>: Stores data in memory</li>
          <li><code>load(key)</code>: Retrieves data from memory</li>
          <li><code>exists(key)</code>: Checks if a key exists</li>
          <li><code>get_all()</code>: Retrieves all stored data</li>
        </ul>
        
        <h3 className="text-xl font-semibold mt-6 mb-3">2. Research Agent</h3>
        <p>
          The ResearchAgent class uses Scrapybara to:
        </p>
        <ul className="list-disc ml-6 my-3">
          <li>Launch a cloud-based Ubuntu instance and browser</li>
          <li>Search Wikipedia for specified topics</li>
          <li>Extract relevant content from web pages</li>
          <li>Take screenshots as evidence</li>
          <li>Store research data in shared memory</li>
        </ul>
        
        <h3 className="text-xl font-semibold mt-6 mb-3">3. Notes Agent</h3>
        <p>
          The NotesAgent class processes research data to:
        </p>
        <ul className="list-disc ml-6 my-3">
          <li>Retrieve research from shared memory</li>
          <li>Format the content into structured notes</li>
          <li>Write notes to a text file</li>
          <li>Create a summary of all research topics</li>
        </ul>
        
        <h3 className="text-xl font-semibold mt-6 mb-3">4. Workflow</h3>
        <ol className="list-decimal ml-6 my-3">
          <li>The main script initializes the shared memory and agents</li>
          <li>For each topic in the configuration:
            <ul className="list-disc ml-6">
              <li>The Research Agent searches for information</li>
              <li>The Notes Agent processes the data and writes notes</li>
            </ul>
          </li>
          <li>After all topics are researched, a summary is generated</li>
          <li>Resources are properly cleaned up</li>
        </ol>
        
        <h2 className="text-2xl font-bold mt-8 mb-4">Bounty Fulfillment</h2>
        <p>
          This project fulfills the Scrapybara "Collaborative Agents" bounty requirements by:
        </p>
        <ul className="space-y-2 my-4">
          <li className="flex items-start">
            <CheckCircle className="h-5 w-5 mr-2 text-green-500 flex-shrink-0 mt-0.5" />
            <span>Using Scrapybara technology for web research</span>
          </li>
          <li className="flex items-start">
            <CheckCircle className="h-5 w-5 mr-2 text-green-500 flex-shrink-0 mt-0.5" />
            <span>Implementing multiple agents (Research + Notes) working toward a common goal</span>
          </li>
          <li className="flex items-start">
            <CheckCircle className="h-5 w-5 mr-2 text-green-500 flex-shrink-0 mt-0.5" />
            <span>Creating a general framework for agent collaboration</span>
          </li>
          <li className="flex items-start">
            <CheckCircle className="h-5 w-5 mr-2 text-green-500 flex-shrink-0 mt-0.5" />
            <span>Demonstrating one agent conducting research while another writes notes to a text file</span>
          </li>
        </ul>
      </div>
    </div>
  );
}