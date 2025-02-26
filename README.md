# Batch Export

**Batch Export** allows you to export multiple objects from a `.blend` file to separate files in one click. Supports: **FBX, OBJ, glTF, STL**.

You can access it from multiple locations:
- **Top Bar** (under File menu)
- **3D Viewport Side Panel** (under the Export tab)

---

## 📝 Features
✅ Export **selected objects** or the **entire collection** the active object belongs to.  
✅ Choose from multiple formats: **FBX, OBJ, glTF (.glb), STL**.  
✅ Add **prefix** and **suffix** to filenames.  
✅ Option to **move objects to origin** before export.  
✅ Option to **apply modifiers** before export.  
✅ Quick access through the **Top Bar menu** and **3D Viewport side panel**.

---

## 📥 Installation
1. Download the `batch_export.py` script.
2. In Blender, go to **Edit > Preferences > Add-ons > Install**.
3. Select the downloaded script and install it.
4. Enable the **Batch Export** add-on in the add-ons list.

---

## 🚀 How to Use
### Accessing the Add-on
- **Top Bar:** Go to **File > Batch Export**.
- **3D Viewport:** Press `N` to open the side panel, navigate to the **Export** tab.

### User Interface
![Top Bar Access](https://user-images.githubusercontent.com/65431647/147272597-7ed290c6-51b4-4afa-a8ee-ee4661330825.png) ![Side Panel Access](https://user-images.githubusercontent.com/65431647/147272883-0c8c10d7-062f-4737-8522-55a3c51c5c50.png)

---

## ⚙️ Settings Overview
### 📂 Files
- **Export Directory:** Folder where files will be saved. `//` means the same folder as the `.blend` file.
- **Prefix:** Text added before the object name. Useful for naming conventions like `sm_` for static meshes.
- **Suffix:** Text added after the object name.

### 📝 Export Settings
- **File Format:** Choose from **FBX, OBJ, glTF (.glb), STL**.
- **Export Mode:**
  - **Selected Objects:** Export only the selected objects.
  - **Collection:** Export all objects in the active object's collection.
- **Move to Origin:** Temporarily moves objects to `(0, 0, 0)` before export.
- **Apply Modifiers:** Applies modifiers before export. *(Note: Disables shape key exports)*

### 🔄 Transform Options
- **Set Location:** Moves objects to specified coordinates before export.
- **Set Rotation:** Adjust object rotation to fix import orientation issues.
- **Set Scale:** Uniformly scale objects on export.

---

## 💡 Tips & Tricks
- To save default export settings, configure them and go to **File > Defaults > Save Startup File**.
- Use prefixes like `sm_` or `bp_` for Unreal Engine asset conventions.
- Export collections to quickly separate different environment assets.

---

## 🛠️ Supported Formats and Notes
| Format | Description | Notes |
|--------|-------------|-------|
| FBX    | Widely used for game engines like Unreal and Unity. | Preserves animations and materials. |
| OBJ    | Simple format for static meshes. | No animation support. |
| glTF   | Modern format optimized for real-time engines. | Use `.glb` for binary compactness. |
| STL    | Standard for 3D printing. | Geometry-only format. |

---

## 🧑‍💻 Author
**Adayas**  
[GitHub Repository (Example)](https://github.com/adayas/batch-export) *(Replace with actual link if hosted)*

## 📝 License
MIT License. Feel free to use and modify as needed.

---

Enjoy exporting effortlessly with **Batch Export**! 🚀
