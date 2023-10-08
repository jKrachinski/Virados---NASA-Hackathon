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
3D procedural general routine was based in jongalland World Generator. Few change were make due to satisfy some requisites of this project and match the goal of generating Exoplanets.
Basically the routine had a few subroutines, just like Minecraft World Generator, the most important for this project are:
  1) Noise Generation + Height Map
  2) Heat Map
  3) Moisture Map
  4) Biome Generation

### Noise Generation + Height Map
Noise were generated using Perlin Noise mathematical model for any given random seed. Next, it generates a Height map based on the Noise generated in the previous procedure. Then bitmasking were used to make more realistic textures. The final result looks like the figure bellow.

![image](https://github.com/jKrachinski/Virados---NASA-Hackathon/assets/129566256/c86b35e2-cfa5-4aef-8d6e-7a47deaaca8e)

The code refered befores uses the library Accidental Noise to deal with Noise related operations (See HeatMap and MoistureMap).
### Heat Map
Heat Map were generated by crossing three diferent MapData. The first one is a gradient: hotter near equator and colder near poles. The second one is a fractal randomly generated by any given seed and some parameters (HeatOctaves and HeatFrequency also uses Perlin Noise). Last one consider corrections related to altitudes. For this purpose it uses correction factors for each altitude, returning as the final result the following figure.

![image](https://github.com/jKrachinski/Virados---NASA-Hackathon/assets/129566256/19984636-71b7-4562-a601-a77dd5ce0787)

### Moisture Map
The Moistue Map generation were similar to the Heat Map. First, it generated a fractal to give us a random base. The data were correct based on altitude (provided by Heigh Map).

![image](https://github.com/jKrachinski/Virados---NASA-Hackathon/assets/129566256/8ce64dcf-df67-4452-a21e-e5962f963791)

### Biome generation
Since Heat Map and Moisture Map are available to provide data, this subroutine uses a classification algorithm using as input Temperature x Moisture and out putting the corresponding Biome (eg. HOT x DRY = Desert). The final map looks like the one presented in this next figure.

![image](https://github.com/jKrachinski/Virados---NASA-Hackathon/assets/129566256/0b328844-71ed-432a-84f4-b8a855f89d47)

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
  
  
