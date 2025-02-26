# 📦 Batch Export Add-on for Blender

**Batch Export** is a Blender add-on that allows you to export multiple objects from your scene to individual files in one click. It provides flexible options for exporting selected objects or entire collections, fixing flipped normals, applying transformations, and controlling the file naming conventions.

---

## 📝 **Features**
✅ Export **selected objects** or the **collection** of the active object.  
✅ Support for common file formats: **FBX, OBJ, glTF (.glb), STL**.  
✅ **Move to Origin:** Temporarily moves objects to the world origin before exporting.  
✅ **Apply Modifiers:** Optionally apply all modifiers before export.  
✅ **Fix Flip Normals:** Recalculates normals to fix inverted normals.  
✅ **File Prefix/Suffix:** Customize exported filenames with prefixes and suffixes.  
✅ Accessible via the **3D Viewport side panel** under the **Export** tab.  

---

## 🗂️ **Installation**
1. Download the `batch_export.zip` file containing the add-on.  
2. In Blender, go to **Edit > Preferences > Add-ons > Install**.  
3. Select the downloaded `.zip` file and click **Install Add-on**.  
4. Enable the add-on named **Batch Export** in the add-ons list.  
5. Access the add-on via the **Export** tab in the 3D Viewport sidebar (`N` key).  

---

## 🚀 **How to Use**
### Accessing the Panel
- Open the 3D Viewport and press `N` to reveal the side panel.
- Navigate to the **Export** tab to find the **Batch Export** section.


---

## ⚙️ **Settings Explained**
### 📂 **Export Settings:**
- **Export Directory:** Select the folder to save exported files. Default: `//` (same as the `.blend` file directory).  
- **File Format:** Choose between **FBX**, **OBJ**, **glTF (.glb)**, or **STL**.  
- **Export Mode:**  
  - **Selected Objects:** Export only the selected objects.  
  - **Collection:** Export all objects in the active object's collection.  
- **File Prefix:** Adds custom text before object names in exported files. *(Example: `sm_` for static meshes.)*  
- **File Suffix:** Adds custom text after object names in exported files.  

### 🧩 **Options:**
- **Move to Origin:** Moves objects to `(0,0,0)` before export and restores position afterward.  
- **Apply Modifiers:** Applies all modifiers to the mesh before exporting. *(Disables shape keys.)*  
- **Fix Flip Normals:** Corrects inverted normals by:  
  1. Moving the 3D cursor to the selected object.  
  2. Setting the object's origin to the cursor.  
  3. Applying location, rotation, and scale.  
  4. Recalculating outside normals in edit mode.  
  5. Restoring the original cursor position.  

---

## 💡 **Tips & Tricks**
- Use the **File Prefix/Suffix** fields to conform to naming conventions for game engines like Unreal Engine or Unity.  
- Enable **Move to Origin** when exporting objects for environments that require centered meshes.  
- **Fix Flip Normals** is essential when exporting models for engines that handle normals differently.  

---

## 🛠️ **Supported Export Formats**
| Format | Extension | Notes |
|--------|-----------|-------|
| FBX    | .fbx      | Compatible with most game engines. Supports animations and materials. |
| OBJ    | .obj      | Widely used for static meshes. No animation support. |
| glTF   | .glb      | Compact and ideal for real-time applications. |
| STL    | .stl      | Common for 3D printing; geometry only. |

---

## 🧑‍💻 **Author**
**Adayas**  
GitHub: [Repository](https://github.com/adayaskm/Blender-Batch-Export)
Version: **1.2.0**  
License: **MIT**  

---

## 📝 **Changelog**
### v1.2.0
- Added **Fix Flip Normals** option with improved pivot and cursor handling.  
- Enhanced UI layout for better usability.  

### v1.1.0
- Added support for **Move to Origin** and **Apply Modifiers** options.  

### v1.0.0
- Initial release with basic export functionality for selected objects and collections.  

---

## 📢 **Feedback & Contributions**
Have suggestions or found a bug? Feel free to open an issue or contribute via pull requests on GitHub! 🚀
