# Project Vision & Scope: CrossPoint Apps

The goal of **CrossPoint Apps** is to create an efficient, open-source reading experience for the Xteink X4, augmented by a suite of high-quality, community-driven applications. We believe an e-reader can be a powerful, distraction-free companion device that goes beyond just reading books—provided the apps are designed with care for the e-ink display and battery life.

## 1. Core Mission

To provide a lightweight, high-performance firmware that maximizes the utility of the X4. We aim to support a thriving ecosystem of apps and tools while maintaining the device's exceptional legibility, long battery life, and distraction-free nature.

## 2. Scope

### In-Scope

*These are features and apps that directly improve the utility of the device while respecting its hardware constraints.*

* **Core Reading Experience:** All upstream CrossPoint features, including EPUB rendering, typography, hyphenation, library management, and local file transfer.
* **Productivity Utilities:** Offline tools like Calculators, Calendars, Clocks, and Dice rollers that are useful to have on a secondary, distraction-free screen.
* **E-Ink Games:** Turn-based, slow-paced games like Chess, Sudoku, or text-based adventures that do not rely on high-framerate animations or color.
* **Offline-First Feeds & Articles:** RSS readers, Reddit clients, Wikipedia browsers, and other information aggregators. These MUST be designed to fetch data via Wi-Fi only when requested, cache the text locally to the SD card, and then disconnect from the network to allow for battery-friendly offline reading.
* **Reference Tools:** Local dictionary lookup, offline documentation viewers, etc.

### Out-of-Scope

*These items are rejected because they compromise the device's stability, battery life, or e-ink constraints.*

* **High-Framerate / Animated Games:** E-ink displays have a slow refresh rate. Action games, platformers, or anything requiring rapid screen updates are fundamentally incompatible with this hardware.
* **Always-Online / Background Polling Apps:** Background Wi-Fi tasks rapidly drain the small battery and complicate the single-core CPU's execution. Apps must not poll servers continuously in the background or require a persistent internet connection to function.
* **Media Playback:** No Audio players or Audio-books. The hardware is not built for this.
* **Complex Typing Apps:** The device lacks a physical keyboard, making long-form typing tedious. Apps should rely primarily on button-driven navigation, D-pads, and simple selections rather than extensive text entry.

## 3. App Evaluation Guidelines

We warmly welcome community contributions! If you want to build an app for CrossPoint Apps, ask yourself the following questions:

1. **Does it work offline?** (If it requires data, does it fetch it efficiently and cache it locally?)
2. **Does it respect the E-ink display?** (Does it avoid animations and unnecessary full-screen refreshes?)
3. **Is it entirely button-navigable?** (Does it have intuitive controls using the physical D-pad layout?)

> **Note to Contributors:** If you have an idea for an app and are unsure if it fits the scope, please open a **Discussion** or issue before you start coding! We are eager to help you design it to fit these guidelines.
