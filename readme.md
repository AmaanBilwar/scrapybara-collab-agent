# Scrapybara Answer Engine

A Perplexity-like answer engine built with Scrapybara, Flask, and Next.js.

## Project Structure

```
.
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js app directory
│   │   ├── components/    # React components
│   │   └── styles/        # CSS styles
│   ├── public/            # Static assets
│   └── package.json       # Frontend dependencies
├── src/                   # Backend source code
│   ├── app.py            # Flask application
│   ├── config.py         # Configuration
│   └── utils/            # Utility functions
├── requirements.txt       # Python dependencies
├── package.json          # Root package.json for scripts
└── run-dev.js            # Development server script
```

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Node.js dependencies:
```bash
npm run install-deps
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```
SCRAPYBARA_API_KEY=your_api_key_here
```

## Development

Run both frontend and backend servers:
```bash
npm run dev
```

This will start:
- Frontend server at http://localhost:3000
- Backend server at http://localhost:5000

## Features

- Real-time answer generation using Scrapybara
- Modern UI with Next.js and Tailwind CSS
- Responsive design
- Loading states and error handling
- Markdown support for answers

## Technologies Used

- **Backend:**
  - Flask
  - Scrapybara SDK
  - Python 3.8+

- **Frontend:**
  - Next.js 13+
  - React
  - Tailwind CSS
  - TypeScript

## License

MIT