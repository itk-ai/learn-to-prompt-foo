# Session 2: Getting Started with Promptfoo

**Goal:** Get your first promptfoo evaluation running with our LLMs

---

## What We'll Do Today

1. ✅ Set up environment variables (API key)
2. ✅ Create your first promptfoo config
3. ✅ Run a simple evaluation
4. ✅ Understand the results

---

## Part 1: Setting Up Your Environment

### Step 1: Create Your Project Folder

Create a new folder on your computer for this exercise:

```
C:\Users\YourName\<projects>\promptfoo-getting-started
```
where `<projects>` is just a folder name where you can collect your VSCode projects - it can be called anything.
Personally in my own setups I called it `git_repos`.

### Step 2: Create `.env` File

Open VSCode inside this folder and from VSCode create a file called `.env` (no name, just `.env` as extension).

For a start the file should just contain
```env name=.env.example
DEV_OWUI_ENDPOINT=
DEV_OWUI_API_KEY=
STG_OWUI_ENDPOINT=
STG_OWUI_API_KEY=
PROD_OWUI_ENDPOINT=
PROD_OWUI_API_KEY=
```

**Why we need this:** The `.env` file is a way to store "local" variables. We will use it to store our API endpoint 
and credentials semi-securely. Promptfoo will read these values when running evaluations.

### Step 3: Get Your API Key

We need to extract your API key from the browser. Follow these steps:

#### 3.1 Open DevTools

1. Open Chrome/Edge browser
2. Navigate to: `https://stgai.itkdev.dk`
3. Press `F12` or right-click → "Inspect" ("Inspicer") or follow:
   ![./sceendumps/edge-dev-tools.png "Tryk F12 eller højre klik på siden og vælg Inspicer"]
4. Click the **Network** tab
   ![./sceendumps/dev-tool-network.png]

**Screenshot placeholder:** DevTools with Network tab visible

#### 3.2 Trigger an API Call

1. In the chat interface, type any question (e.g., "Hej")
2. Send the message
3. In the Network tab, you should see e.g. a `completions` row appear. Click it.

[!./screendumps/edge-dev-find-apikey.png]

#### 3.3 Find the Authorization Header

1. Look for **Headers** tab (usually selected by default)
2. Scroll down to **Request Headers**
3. Find `Authorization` header, as seen in the screenshot above - it will look like:
   ```
   Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```

#### 3.4 Copy the Token

1. Copy the **entire** value after `Bearer ` (including the `eyJ...`)
2. Don't copy the word "Bearer" itself, just the token

### Step 4: Add API Key to `.env`

Open your `.env` file in VSCode and update it:

```txt name=.env.example
DEV_OWUI_ENDPOINT=
DEV_OWUI_API_KEY=
STG_OWUI_ENDPOINT=https://stgai.itkdev.dk
STG_OWUI_API_KEY=<eyJhbGciO... something your actual token goes here>
PROD_OWUI_ENDPOINT=
PROD_OWUI_API_KEY=
```

## Exercise

Do the same for [ai.aarhuskommune.dk](https://ai.aarhuskommune.dk) and obtain the api key / token for 
the production site (and update the .env-file variables `PROD_OWUI_ENDPOINT` and `PROD_OWUI_API_KEY`).

---

## Part 2: Get started with promptfoo

### Step 1: Fetch the getting started example

In VSCode, in the same folder (`promptfoo-getting-started`), create a file called `promptfooconfig.yaml`.

