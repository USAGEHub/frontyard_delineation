# 🏡 Front Yard Delineation Tool

This tool addresses the complex problem of automatically delineating **front** (and potentially **back**) yards for residential parcels, based on spatial relationships between buildings and roads.

## 🔍 Overview

The goal is to split residential parcels into front and back yard polygons by identifying the facade of buildings facing the road and using that orientation to divide the land.

## 💡 Methodology

1. **Filter input data**: Use only residential parcels (pre-filtered in earlier steps).
2. **Extract facade points** (_gevelpunten_) from building footprints.
3. **Calculate shortest distance** from each facade point to the nearest road segment.
4. **Select the two closest points** and export them.
5. **Draw a connecting line** between the two selected points.
6. **Extend this line** until it intersects with the parcel boundary.
7. **Split the parcel** polygon using this extended line.
8. **Export the front yard** (the side facing the road).

## 🔄 Potential Extension: Back Yard Extraction

The same logic could be applied in reverse—using the two **furthest** points from the road—to delineate **back yards**.

## 🚧 Known Challenges & Future Improvements

- 🏢 **Multiple addresses per parcel**: Common in apartment complexes, complicating front yard assignment.
- 🛣️ **Segmented and bending roads**: Roads are not continuous lines, which affects distance measurement and orientation.
- 📍 **Address-road matching**: Improvement could be made by linking address points to parcels and calculating distance to the **corresponding** road segment instead of the nearest arbitrary segment.

## 📁 Required Inputs

- 🗂️ Residential parcel polygons  
- 🏠 Building footprints or facade points (_gevelpunten_)  
- 🛣️ Road network (line geometries)  
- 📌 (Optional) Address points  

## 🧾 Output

- ✅ Geo-referenced front yard polygons (e.g., GeoJSON, SHP)

---

Feel free to open issues or submit pull requests to improve the tool.
