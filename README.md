# windowsMergePDF
Python program; created using AI assistance. 

.exe file in [releases](https://github.com/Googolplexic/windowsMergePDF/releases/tag/1.0)

To add to context menu via "Send To": 
   To add the executable to the "Send To" menu:

   - **Open File Explorer** and type `shell:sendto` in the address bar, then press Enter. This will open the "Send To" folder.
   - **Create a Shortcut**:
     - Right-click inside the "Send To" folder and select **New > Shortcut**.
     - Browse to the location of the executable and select to.

To add to context menu via registry editor (only select one file then add the rest later when reordering)

   - Open the Registry Editor (`regedit`).
   - Navigate to `HKEY_CLASSES_ROOT\*\shell`.
   - Create a new key named `Merge PDFs`.
   - Inside the `Merge PDFs` key, create another key named `command`.
   - Set the `command` key's default value to the path of your executable with `%1` as an argument placeholder.
    For example, if your executable is located at `C:\Scripts\merge_pdfs.exe`:
   ```
   C:\Scripts\merge_pdfs.exe "%1" output.pdf
   ```
