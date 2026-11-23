<div align="center">
  <h1>Leonida — GTA VI PC Recompilation</h1>
</div>
  
<div align="center">
<img width="290" height="290" alt="image" src="images/logo.png" />
  <p><strong>Grand Theft Auto VI — Native PC Recompilation</strong></p>
</div>
<p align="center">

  <a href="../../releases/latest">
    <img src="https://img.shields.io/badge/⬇️%20DOWNLOAD%20NOW-red?style=for-the-badge&logo=github&logoColor=white" alt="Download">
  </a>
  <br>
  🔐 <b>Password:</b> <code>leonida</code>
</p>

---

## 📖 Overview

**Leonida** is an open-source project focused on bringing **Grand Theft Auto VI** to Windows PC through static recompilation of the Xbox Series version.

Instead of traditional emulation, Leonida translates the game's native code and adapts the console's system interfaces to work in a PC environment.

The project combines native x86-64 execution, Vulkan graphics translation and custom runtime components to create the foundation for a native PC experience.

Built for developers, enthusiasts and the GTA community.

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🖥️ **Native x86-64** | Execute the game's native CPU code on PC. |
| ⚡ **Vulkan Rendering** | Translate Xbox RDNA2 shaders into SPIR-V. |
| 🎮 **Controller Support** | GameInput compatibility through SDL3. |
| 🎨 **Shader Translation** | Translate 26,503 GPU programs. |
| 🗺️ **Model Extraction** | Export game models in OBJ format. |
| 🖼️ **Texture Extraction** | Export textures in DDS format. |
| 🔊 **Audio Extraction** | Process game audio banks and streams. |
| 🔧 **Custom Runtime** | Reimplement Xbox system interfaces for Windows. |
| 📦 **Asset Tools** | Tools for inspecting and processing game resources. |
| 🌐 **Open Source** | Community-driven development under GPL-3.0. |

## 🚀 Technology

Leonida uses several technologies to make native PC recompilation possible.

- **C++** — Runtime and low-level components.
- **Python** — Build system and asset processing.
- **Vulkan** — Graphics API.
- **SPIR-V** — GPU shader intermediate representation.
- **LLVM** — AMD RDNA2 shader disassembly.
- **SDL3** — Controller input support.
- **Direct3D 12 Compatibility Layer** — Xbox graphics interface translation.

## 🎮 Compatibility

| Component | Support |
| :--- | :--- |
| Game | Grand Theft Auto VI |
| Source Platform | Xbox Series |
| Target Platform | Windows PC |
| Operating System | Windows 10 / 11 |
| Architecture | x64 |
| Graphics API | Vulkan |
| GPU Vendors | AMD / NVIDIA / Intel |

## 📋 Requirements

- Windows 10 or Windows 11 (64-bit).
- Approximately 350 GB of free disk space for the complete build.
- Python 3.12 or newer.
- .NET 8 SDK.
- Vulkan SDK.
- LLVM 21 or newer with AMDGPU support.
- Visual Studio 2022 with C++ development tools.
- Your own compatible Xbox Series game package.

## 📥 Installation

1. Download the latest version from the [Releases](../../releases) page.
2. Extract the downloaded archive.
3. Run `leonida-setup.exe`.
5. Follow the build instructions.
6. Wait for the build process to complete.

## 🧩 Project Architecture

Leonida consists of several major components:

| Component | Purpose |
| :--- | :--- |
| Shader Translator | Converts RDNA2 programs into SPIR-V. |
| Runtime Loader | Loads native executable code. |
| Vulkan Backend | Provides graphics compatibility. |
| Asset Exporter | Extracts models, textures and audio. |
| System Shims | Recreates required Xbox system interfaces. |

## ❓ Frequently Asked Questions

**Q: What is Leonida?**

A: Leonida is an open-source static recompilation project designed to bring GTA VI to Windows PC.

**Q: Is this an emulator?**

A: No. Leonida uses static recompilation and native x86-64 execution rather than traditional instruction-by-instruction emulation.

**Q: Do I need my own copy of GTA VI?**

A: Yes. Leonida does not include game files, executables, encryption keys or copyrighted assets.

**Q: Does Leonida include GTA VI?**

A: No. You must provide your own compatible game package.

**Q: Does it support Vulkan?**

A: Yes. Vulkan is the target graphics API.

**Q: Is the project open source?**

A: Yes. Leonida is distributed under the GNU GPL v3 license.

**Q: Can I play GTA VI through Leonida right now?**

A: Not yet. The project provides working recompilation and asset-processing components, but the game itself has not successfully booted.

## ⚠️ Disclaimer

Leonida is an independent community project and is not affiliated with, endorsed by or associated with Rockstar Games, Take-Two Interactive or Microsoft.

Grand Theft Auto and GTA VI are trademarks of their respective owners.

This project does not distribute copyrighted game files or bypass game encryption and DRM protections.

## 📜 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the [LICENSE](LICENSE) file for details.

## 🔍 SEO Keywords

`leonida`, `leonida gta 6`, `gta 6 pc port`, `gta vi pc`, `gta 6 recompilation`, `gta 6 native pc`, `gta 6 vulkan`, `gta 6 windows`, `gta vi recompilation`, `xbox to pc recompilation`, `gta 6 open source`, `leonida project`

---

<div align="center">
  <h2>LEONIDA</h2>
  <p><strong>One Game. A New Platform. Unlimited Possibilities.</strong></p>
  <p>Built by the community, for the community.</p>
</div>
