# Simple FFmpeg (Simple Mass FFmpeg GUI)

A simple Python application (Tkinter-based) to **batch convert and modify videos** in a folder using FFmpeg — without typing complex terminal commands!

> ⚠️ Currently supports **Windows only** (uses batch scripts and `cmd`).

---

## 🚀 Features

✅ **Folder Selection:** Easily select input and output folders.

✅ **Video Rotation:** Rotate videos by 0°, 90°, 180°, or 270°.

✅ **Video Flipping:** Flip videos horizontally or vertically.

✅ **Format Conversion:** Specify input and output file formats (e.g., mp4, avi).

✅ **Live Preview:** See a live preview of how transformations will affect your videos (based on a sample image).

✅ **Automation:** Automatically generates and executes the correct FFmpeg batch command.

✅ **FFmpeg Installer:** One-click FFmpeg installer (using `winget`).

---

## 💻 Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Jachu7/simple-ffmpeg.git
    cd simple-mass-ffmpeg
    ```

2.  **Install Python dependencies:**

    ```bash
    pip install Pillow
    ```

3.  **(Optional) Install FFmpeg:**

    You can install FFmpeg directly from the app (button at the top), or manually:

    ```bash
    winget install ffmpeg
    ```

---

## ⚙️ How to Use

1.  **Run the application:**
    Open a terminal or command prompt, navigate to the directory where you saved the script, and run:

    ```bash
    python main.py
    ```

2.  **Select folders and options:**

    * Select the **input folder** containing your videos.
    * Select the **output folder** for the converted videos.
    * Choose the desired **rotation** and **flip** options.
    * Enter the **input** and **output** file formats.

3.  **Preview:**
    The "Preview what will happen with your videos based on image below" section will show a visual representation of the selected transformations on a sample image.

4.  **Execute command:**
    Once you've configured all options, click the "Execute in terminal" button. This will generate the FFmpeg command and execute it in a new command prompt window, processing your videos.

---

## 🧰 Requirements

* Windows 10/11
* Python 3.x (3.8+ recommended)
* FFmpeg installed (or install via the app button)

---

## 📸 Screenshots

![App Preview](assets/preview.jpg)


---

## 🙏 Acknowledgements

* [FFmpeg](https://ffmpeg.org/)
* [Python Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Pillow](https://pypi.org/project/pillow/)

---

## 💬 License

[MIT License](https://opensource.org/licenses/MIT) — free to use and modify.

---

## ⭐️ Contributing

Pull requests are welcome! If you'd like to improve or add features, feel free to fork the repository and open a PR.

---

## 📩 Questions?

Open an [issue on GitHub](https://github.com/Jachu7/simple-ffmpeg/issues) or contact me directly!