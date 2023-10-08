# Virados - Exoplanets Smart Generator
This project aims to generate by procedural generation a 3d map representing an exoplanet and to plot a dashboard with some relevant maps about this world.

#Feature list 
- 3D rendering procedural generated planet
- Dashboard containing data about the planet
- AI generated text description about daily life in the planet respecting Astrobiological Concepts
- AI generated landscape image inside of the planet

## Relevance
{HERE SOME TEXT}

## 3D Procedural Generation
{HERE SOME TEXT}

## AI Generation
The AI generations was obtained through the Eden AI free API key, in order to generate both images and text descriptions of the 3D envionments. In order to do so, the 3D procedural generetion would create a certain amount of key-words, which would describe the world just generated. These words woulds involve, the average terrain of the planet, the biomes present, humidity, average temperature and other relevant data.

**generate_image(prompt)**
This funciton is called in order to generate an image based on the string prompt provided by the function caller.
It returns the link in which the image can downloaded into the user's computer.

**generate_text(prompt)**
This funciton is called in order to generate a text based on the string prompt provided by the function caller.
It returns AI generated response.

**CreateDescription**
This Class creates an image, a brief and a long description of a planet, based on the AI generated output, as well as it creates a json file with the output.
  
  
