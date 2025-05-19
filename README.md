# LoL Skin Quiz

A web app that challenges you to guess League of Legends skin names by their splash arts. Built with Python + Flask.

## How to Set It Up

Follow these steps to run the app locally:

1. **Download the splash arts**
   - Visit the [Google Drive](https://drive.google.com/drive/folders/14S9RQJ63pYQPXB9RFZSZgWkk5-qHbs_i?usp=sharing)
   - Download the ZIP containing splash art images

2. **Unzip the package**
   - Extract the contents anywhere on your computer

3. **Create the splash folder**
   - Inside the project folder, create a folder at: `./static/splash`

4. **Move the images**
   - Move all the `.jpg` images into `static/splash/`

5. **Install Flask**
   - Make sure you have Python 3 installed
   - Then install Flask via terminal:
     ```bash
     pip install flask
     ```

6. **Generate `skins.json`**
   - This step extracts clean skin names from your image filenames:
     ```bash
     python generate_names.py
     ```

7. **Run the app**
   - Start the server:
     ```bash
     flask run
     ```
   - Visit the link that pops out in the terminal.

## How to Play

- A splash art will be shown.
- Type the name of the skin in the input box (case doesn't matter).
- Click **Guess** — or **Surrender** to see the answer.
- Your **streak** increases with each correct guess and resets on surrender.
- Images won’t repeat immediately.

## Skin Name Format

The `generate_names.py` script converts filenames like:
Ahri_OriginalSkin_HD.jpg
Warwick_PROJECTSkin_HD.jpg

Into this:

```json
{
  "Ahri_OriginalSkin_HD.jpg": "Ahri",
  "Warwick_PROJECTSkin_HD.jpg": "PROJECT Warwick"
}
```

## Credits

- Splash art images © Riot Games  
- All League of Legends characters, skins, and artwork are the property of Riot Games  
- This project is fan-made and not affiliated with Riot Games in any way  
  [Riot Games website](https://www.riotgames.com/en)

## Sources

All splash arts were downloaded from:

[Reddit: High-Quality Splash Art Collection](https://www.reddit.com/r/leagueoflegends/comments/19e9m33/google_drive_link_with_highquality_splash_art_for)

## Built With

- Python 3
- Flask
- Tailwind CSS (via CDN)

## License

- MIT License for code  
- No commercial redistribution of splash arts

## Legal Disclaimer

This is a personal, fan-made project.  
All League of Legends splash arts and champion designs are © Riot Games.  
They are used here under Riot's [Legal Guidelines](https://www.riotgames.com/en/legal) for non-commercial fan content.
