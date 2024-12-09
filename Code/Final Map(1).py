import folium
import pandas as pd
from folium import LinearColormap
import requests

# Load the processed CSV file to extract country names and ASR values
processed_data = pd.read_csv('Processed_Breast_World.csv')

# Define the data for selected countries with extra information
selected_countries_data = {
    "United States of America": {
        "lat": 37.0902,
        "lon": -95.7129,
        "asr_value": 95.91,  # ASR (World) per 100 000
        "genes": ["EGFR", "LEP", "FN1", "BMP2", "TGFBR2"],
        "url": "https://version-12-0.string-db.org/cgi/network?networkId=bsbfPDFY8w5m",
        "string_img": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/USA/USA.png",
        "step_1_links": [
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE10780",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE15852",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE42568"
        ],
        "step_2_links": [
            "https://laurisisme.github.io/GSE10780_USA/",
            "https://laurisisme.github.io/GSE15852_USA/",
            "https://laurisisme.github.io/GSE42568_USA/"
        ],
        "step_3_images": [
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/USA/log_USA.png",
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/USA/xgboost_USA.png"
        ],
        "step_4_image": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/USA/KEGG_USA.png",
        "step_2_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/USA/Step1_USA.csv",  # New link for Step 2
        "step_3_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/USA/Step2_USA.csv",
        "step_4_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/USA/Filtered_Genes_KEGG_USA.csv",
        "step_4_additional_link": "https://github.com/YP-118/Info301_Final/blob/main/Data/USA/KEGG_Enrichment_Results_USA.csv"
    },
    "China": {
        "lat": 35.8617,
        "lon": 104.1954,
        "asr_value": 33.04,
        "genes": ["CDC25A", "CCNE2", "CDC7", "CDKN2A", "MME"],
        "url": "https://version-12-0.string-db.org/cgi/network?networkId=bt8a7mFOzihu",
        "string_img": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/China/China.png",
        "step_1_links": [
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE210787",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229571",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE271851"
        ],
        "step_2_links": [
            "https://laurisisme.github.io/GSE210787_China/",
            "https://laurisisme.github.io/GSE229571_China/",
            "https://laurisisme.github.io/GSE271851_China/"
        ],
        "step_3_images": [
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/China/log_chi.png",
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/China/xgboost_chi.png"
        ],
        "step_4_image": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/China/KEGG.png",
        "step_2_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/China/Step1_China.csv",  # New link for Step 2
        "step_3_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/China/Step2_China.csv",
        "step_4_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/China/Filtered_Genes_KEGG_China.csv",
        "step_4_additional_link": "https://github.com/YP-118/Info301_Final/blob/main/Data/China/KEGG_Enrichment_Results_China.csv"
    },
    "Australia": {
        "lat": -25.2744,
        "lon": 133.7751,
        "asr_value": 101.47,
        "genes": ["JUN", "PTGS2", "IL18", "PLAU", "STAT1"],
        "url": "https://version-12-0.string-db.org/cgi/network?networkId=bWXuEE2LKLBa",
        "string_img": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/Australia/Australia.png",
        "step_1_links": [
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE10782",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE61725",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE123762"
        ],
        "step_2_links": [
            "https://laurisisme.github.io/GSE10782_Australia/",
            "https://laurisisme.github.io/GSE61725_Australia/",
            "https://laurisisme.github.io/GSE123762_Australia/"
        ],
        "step_3_images": [
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/Australia/SHAP_Log.png",
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/Australia/SHAP_XGBoost.png"
        ],
        "step_4_image": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/Australia/KEGG.png",
        "step_2_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/Australia/Step1_Australia.csv",  # New link for Step 2
        "step_3_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/Australia/Step2_Australia.csv",
        "step_4_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/Australia/Filtered_Genes_KEGG_Australia.csv",
        "step_4_additional_link": "https://github.com/YP-118/Info301_Final/blob/main/Data/Australia/KEGG_Enrichment_Results_Australia.csv"
    },
    "France": {
        "lat": 46.6034,
        "lon": 1.8883,
        "asr_value": 105.42,
        "genes": ["SMAD3", "TGFBR2", "SMAD9", "COX4I2", "COX4I1"],
        "url": "https://version-12-0.string-db.org/cgi/network?networkId=bW8BGC1m8TJ5",
        "string_img": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/France/France.png",
        "step_1_links": [
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE31448",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE45827",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65194"
        ],
        "step_2_links": [
            "https://laurisisme.github.io/GSE31448_France/",
            "https://laurisisme.github.io/GSE45827_France/",
            "https://laurisisme.github.io/GSE65194_France/"
        ],
        "step_3_images": [
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/France/log_France.png",
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/France/xgboost_France.png"
        ],
        "step_4_image": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/France/KEGG_France.png",
        "step_2_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/France/Step1_France.csv",  # New link for Step 2
        "step_3_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/France/Step2_France.csv",
        "step_4_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/France/Filtered_Genes_KEGG_France.csv",
        "step_4_additional_link": "https://github.com/YP-118/Info301_Final/blob/main/Data/France/KEGG_Enrichment_Results_France.csv"
    },
    "Japan": {
        "lat": 36.2048,
        "lon": 138.2529,
        "asr_value": 74.39,
        "genes": ["TGFA", "SPP1", "PLAU", "PDGFA", "COL10A1"],
        "url": "https://version-12-0.string-db.org/cgi/network?networkId=b4IUYnkUodZy",
        "string_img": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/Japan/Japan.png",
        "step_1_links": [
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE38959",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE54002",
        ],
        "step_2_links": [
            "https://laurisisme.github.io/GSE38959_Japan/",
            "https://laurisisme.github.io/GSE54002_Japan/",
        ],
        "step_3_images": [
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/Japan/log_jap.png",
            "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/Japan/xgboost_jap.png"
        ],
        "step_4_image": "https://raw.githubusercontent.com/YP-118/Info301_Final/main/Visualization/Japan/KEGG_Jap.png",
        "step_2_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/Japan/Step1_Japan.csv",  # New link for Step 2
        "step_3_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/Japan/Step2_Japan.csv",
        "step_4_filtered_genes": "https://github.com/YP-118/Info301_Final/blob/main/Data/Japan/Filtered_Genes_KEGG_Japan.csv",
        "step_4_additional_link": "https://github.com/YP-118/Info301_Final/blob/main/Data/Japan/KEGG_Enrichment_Results_Japan.csv"
    },
}


# GeoJSON URL from GitHub (if accessible)
geojson_url = "https://raw.githubusercontent.com/datasets/geo-countries/main/data/countries.geojson"
response = requests.get(geojson_url)
geojson_data = response.json()
# Create a map centered on the world
world_map = folium.Map(
    location=[20, 0],
    zoom_start=2,
    tiles="cartodbpositron",
    no_wrap=True,
    world_copy_jump=False
)

# Create the color scale (LinearColormap)
colormap = LinearColormap(
    colors=["#ffffff", "#ffcccc", "#ff6666", "#ff0000"],
    vmin=processed_data['ASR (World) per 100 000'].min(),
    vmax=processed_data['ASR (World) per 100 000'].max()
)

# Function to dynamically style countries based on ASR (World) per 100 000 for all countries
def style_function(feature):
    country_name = feature["properties"]["ADMIN"]
    country_row = processed_data[processed_data['Corrected Country'] == country_name]
    if not country_row.empty:
        asr_value = country_row['ASR (World) per 100 000'].values[0]
        color = colormap(asr_value)
        return {"fillOpacity": 0.6, "weight": 0.5, "fillColor": color, "color": "black"}
    return {"fillOpacity": 0.1, "weight": 0.5, "fillColor": "gray", "color": "black"}

# Add GeoJSON layer for country boundaries
folium.GeoJson(
    geojson_data,
    name="Countries",
    style_function=style_function,
).add_to(world_map)

# Create a JavaScript function for the modal
modal_js = """
    <script>
    function showModal(imageSrc) {
        var modal = document.createElement('div');
        modal.style.position = 'fixed';
        modal.style.top = '0';
        modal.style.left = '0';
        modal.style.width = '100%';
        modal.style.height = '100%';
        modal.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
        modal.style.display = 'flex';
        modal.style.alignItems = 'center';
        modal.style.justifyContent = 'center';
        modal.style.zIndex = '1000';
        modal.onclick = function() {
            modal.remove();
        };

        var img = document.createElement('img');
        img.src = imageSrc;
        img.style.maxWidth = '80%';
        img.style.maxHeight = '80%';
        img.style.borderRadius = '10px';

        modal.appendChild(img);
        document.body.appendChild(modal);
    }
    </script>
"""

# Add the modal JavaScript to the map's HTML header
world_map.get_root().html.add_child(folium.Element(modal_js))

# Add markers for selected countries (Only USA for now)
for country, info in selected_countries_data.items():
    # Start constructing the popup content
    popup_content = f"""
    <strong>{country}</strong><br>
    <strong>ASR Value:</strong> {info['asr_value']}<br>
    <strong>Top Genes:</strong> {", ".join(info['genes'])}<br>

    <strong>Step 1: Links to NCBI</strong><br>
    """

    # Loop through the step_1_links and create dynamic links
    for i, link in enumerate(info['step_1_links']):
        # Extract the identifier from the link (after "acc=")
        link_id = link.split("=")[-1]
        # Add a link to the popup content with the identifier (e.g., GSE10780)
        popup_content += f'<a href="{link}" target="_blank">{link_id}</a>'

        # Add pipe separator except for the last link
        if i < len(info['step_1_links']) - 1:
            popup_content += " | "

    popup_content += f"<br>"

    # Step 2: Cross Evaluation (Dynamic Links)
    popup_content += f"""
    <strong>Step 2: Cross Evaluation</strong><br>
    <a href="{info.get('step_2_filtered_genes', '#')}" target="_blank">View filtered genes</a><br>
    """
    for i, link in enumerate(info['step_2_links']):
        # For Step 2, use "Heatmap" for each link
        popup_content += f'<a href="{link}" target="_blank">Heatmap {i+1}</a>'

        # Add pipe separator except for the last link
        if i < len(info['step_2_links']) - 1:
            popup_content += " | "

    popup_content += f"<br>"

    # Step 3: Machine Learning (Dynamic links + View filtered genes)
    popup_content += f"""
    <strong>Step 3: Machine Learning</strong><br>
    <a href="{info.get('step_3_filtered_genes', '#')}" target="_blank">View filtered genes</a><br>
    <img src="{info['step_3_images'][0]}" alt="Gene Expression Log" width="100" style="margin-right: 10px; cursor: pointer;" onclick="showModal('{info['step_3_images'][0]}')">
    <img src="{info['step_3_images'][1]}" alt="Gene Expression XGBoost" width="100" style="cursor: pointer;" onclick="showModal('{info['step_3_images'][1]}')"><br>
    """

    # Step 4: KEGG Pathway (Dynamic link)
    popup_content += f"""
    <strong>Step 4: KEGG Pathway</strong><br>
    <a href="{info.get('step_4_additional_link', '#')}" target="_blank">KEGG Pathway Info</a>
    <a href="{info.get('step_4_filtered_genes', '#')}" target="_blank">View filtered genes</a><br>
    <img src="{info['step_4_image']}" alt="KEGG Pathway" width="200" style="cursor: pointer;" onclick="showModal('{info['step_4_image']}')"><br>
    """

    # Step 5: PPI (Dynamic link)
    popup_content += f"""
    <strong>Step 5: PPI</strong><br>
    <img src="{info['string_img']}" alt="STRING Image" width="200" style="cursor: pointer;" onclick="showModal('{info['string_img']}')"><br>
    <a href="{info['url']}" target="_blank">Visit STRING Database</a>
    """

    # Add the marker for the country
    folium.Marker(
        location=[info["lat"], info["lon"]],
        popup=folium.Popup(popup_content, max_width=600),
        tooltip=f"Click for {country} details",
    ).add_to(world_map)

# Add an additional green marker in the middle of the Atlantic Ocean
folium.Marker(
    location=[0, -30],  # Coordinates in the middle of the Atlantic Ocean
    popup=folium.Popup(
        """
        <strong>Number of Datasets Found:</strong> <a href="https://laurisisme.github.io/countrydataset/" target="_blank">See plot</a>

        """,
        max_width=300
    ),
    icon=folium.Icon(color='green', icon='info-sign')  # Green marker
).add_to(world_map)

# Save the map to an HTML file
map_path = "map.html"
world_map.save(map_path)
map_path