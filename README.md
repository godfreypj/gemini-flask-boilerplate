# Gemini Flask App

## 🧠 Overview
This application is based entirely off of [Google's Project IDX](https://idx.dev/) Gemini Web App. I wanted an even better boilerplate that wasn't tied to the IDX system.

## 🍄 Flask:
This app is a very simple Flask API. It's broken into 2 sections:
### - `main`
#### `/`
The main route will automatically load up the swagger ui docs.

#### `/api/generate`
The `generate` route will take the prompt & training data (provided separately) and add an expected return format before sending the request to the LLM. Once returned, it will format the response (based off the expected return format) before returning the result.

#### `/<path:path>`
This is the built in route to serve static files from the `web` directory. Check out `/health.html` for an example.

### - `utils`
Main needs these functions to do its job:
- `load_prompt`
    - The expectation is that you supply a prompt in the form of a `.txt` file in the `data` directory. This will read in the prompt and add in expected response format.
- `load_training_data`:
    - The expectation is that you supply examples of training data in the form of `.txt` files in the `data` directory.
- `format_response`:
    - `load_prompt` supples an expected response format - assuming that we can parse the LLMs response into something easy to return.

## 🗒️ Configuration
The `.env` file contains the following environment variables:
```bash
API_KEY = 'YOUR_API_KEY'
MODEL = 'YOUR_MODEL' # (defaults to flash)
```
♩NOTE: The `.env` file is in version control for ease of configuration but you can un-comment that line in the `.gitignore`.

## 🖋️ Documentation
I love docs. So I decided to include a SwaggerUI page as well. Remember to use documentation. I also included a default `route`, which will return the swaggerui as `index.html` as well as the `health.html` endpoint as static page example.

## 🦒 Getting Started
1. Fill in the `.env` file with the appropriate settings.
2. Run:
```bash
pip install -r requirements.txt
./devserver.sh 5000
curl -X GET http://127.0.0.1:5000/api/generate
```
3. You can also navigate to http://127.0.0.1:5000/ to view the SwaggerUI docs.
4. You can also navigate to http://127.0.0.1:5000/health.html to see how the static server works.
