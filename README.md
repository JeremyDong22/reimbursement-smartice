# Reimbursement Tracker - Smartice

A Progressive Web App (PWA) for tracking and managing expense reimbursements with real-time sync powered by Supabase.

## Features

- 💼 Track expenses by category
- 💱 Automatic USD to RMB conversion
- 📊 Export to CSV
- 📱 Works offline (PWA)
- 🔄 Real-time sync with Supabase
- 📜 Payment history tracking

## Quick Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/reimbursement-smartice)

## Installation

### As a PWA

1. Visit the deployed URL
2. Click the install icon in your browser's address bar
3. Or on mobile: Menu → "Add to Home Screen"

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/reimbursement-smartice.git

# Navigate to project
cd reimbursement-smartice

# Start a local server
python3 -m http.server 8080
# or
npx http-server -p 8080

# Open http://localhost:8080
```

## Technology Stack

- HTML5 & JavaScript (Vanilla)
- Supabase (Backend & Database)
- PWA (Service Worker for offline support)
- Vercel (Deployment)

## Environment Setup

The app uses Supabase for backend. The API keys are already configured in the code for the demo instance.

## Icon

The app uses a custom monkey mascot icon that displays when installed as a PWA.

## License

MIT