
# Screenshot and Note-Making Tool

A desktop application for capturing screenshots, making notes, generating flashcards, and debugging code using AI. This app combines Python (Flask) for backend logic and Electron (Vue-based) for the frontend interface, providing a seamless note-taking experience with AI-powered code assistance.

## Project Structure

```
ScreenshotNoteApp/
├── backend/
│   ├── app.py            # Flask backend API
│   ├── data.db           # SQLite database (auto-created on first run)
│   ├── .env              # Environment file for sensitive data
├── frontend/
│   ├── main.js           # Electron main file
│   ├── preload.js        # Electron preload script
│   ├── index.html        # Frontend interface using Vue
├── package.json          # Electron dependencies and configuration
└── README.md             # Project documentation
```

## Features

- **Screenshot Capture**: Capture screenshots using a global hotkey (`Ctrl + Shift + S`).
- **Note-Making**: Add text notes associated with each screenshot.
- **Flashcard Generation**: Convert notes into flashcards for easy review.
- **AI-Powered Code Debugging**: Utilize OpenAI’s ChatGPT to analyze code snippets and provide debugging suggestions.

## Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **Node.js and npm**
- **Tesseract OCR** (for text recognition in screenshots)

### Required Python Packages

Install the following Python packages:

```bash
pip install flask flask-cors pytesseract pillow openai python-dotenv
```

### Required Node.js Packages

Install the Electron framework and `axios` for handling HTTP requests:

```bash
npm install
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/ScreenshotNoteApp.git
   cd ScreenshotNoteApp
   ```

2. **Backend Setup (Flask)**

   - **Environment Variables**: Create a `.env` file in the `backend` folder with your OpenAI API key:

     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

   - **Database**: The `data.db` SQLite database will be created automatically upon running the app.

   - **Run the Flask Server**:

     ```bash
     cd backend
     python app.py
     ```

3. **Frontend Setup (Electron)**

   - **Install Node.js Dependencies**:

     ```bash
     cd ScreenshotNoteApp
     npm install
     ```

   - **Run the Electron App**:

     ```bash
     npm start
     ```

## Usage

1. **Screenshot Capture**: Press `Ctrl + Shift + S` to capture a screenshot, which is saved locally as `screenshot.png`.
2. **Add Notes**: Use the "Add Note" button in the UI to associate a note with the screenshot.
3. **Create Flashcards**: Use the "Add Flashcard" button to create a flashcard from a note.
4. **AI Debugging**: Enter a code snippet using the "Debug Code" button to receive AI-powered debugging suggestions.

## Project Dependencies

### Python Packages

- **Flask** - Backend server for handling requests.
- **Flask-CORS** - Allows cross-origin requests from Electron to Flask.
- **Pillow** - Python Imaging Library, used for screenshot capture.
- **pytesseract** - OCR library for extracting text from images.
- **OpenAI** - API client for AI-powered code debugging.

### Node Packages

- **Electron** - Framework for building cross-platform desktop apps.
- **Axios** - HTTP client for making API requests to the Flask backend.

## Development Notes

- **Global Hotkey**: The hotkey `Ctrl + Shift + S` captures screenshots. Customize this in `main.js` if needed.
- **Database**: All notes and flashcards are stored in `data.db`. This can be changed or configured further in `app.py`.
- **AI Integration**: For AI debugging, ensure your OpenAI API key is configured in `.env`.

## Future Enhancements

- **UI Improvements**: Adding a Vue or React framework for a richer interface.
- **User Authentication**: Integrate login functionality to manage individual user sessions.
- **Advanced OCR**: Expand OCR to identify code blocks and recognize syntax.

---

## Troubleshooting

- **Flask Server Issues**: Ensure the server is running on `http://127.0.0.1:5000`. Restart if there are connection issues.
- **Electron Issues**: Check `package.json` for correct Electron and Axios versions.
- **OpenAI API Errors**: Verify that your API key is active and correctly placed in the `.env` file.

## License

This project is open-source and available under the MIT License.
