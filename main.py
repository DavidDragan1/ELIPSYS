import pyscript
from pyscript import document

tones = {
    # tone1 = history of writing
    'tone1': ['The history of writing and typography unfolds as a rich tapestry, revealing the profound evolution of human communication and the artistic expression of ideas through symbols. From the earliest cave paintings to the digital fonts of the present era, this narrative reflects the inexorable human quest for meaningful connection and the refinement of methods to convey thoughts.',
              'Prehistoric times witnessed the emergence of rudimentary forms of writing, as evidenced by the symbolic cave paintings that depicted aspects of daily life, hunting scenes, and spiritual beliefs. These early pictographs served as the foundational steps toward more structured and systematic modes of communication.',
              'In Mesopotamia, around 3200 BCE, the advent of cuneiform writing marked a pivotal moment in the history of writing. This wedge-shaped script, impressed onto clay tablets with a stylus, enabled the recording of laws, literature, and economic transactions in ancient Sumerian and Akkadian societies.',
              'Simultaneously, the Egyptians developed their hieroglyphic writing system, a complex amalgamation of logographic and alphabetic elements. Hieroglyphs adorned tombs, temples, and monumental structures, serving both practical and ceremonial purposes.',
              'The ancient Greeks introduced the concept of an alphabet, a transformative leap in writing systems. This innovation laid the groundwork for various scripts in Western civilizations and influenced the development of Latin, the precursor to many modern European languages.',
              'The medieval period witnessed the meticulous craftsmanship of scribes who meticulously copied manuscripts by hand, preserving knowledge and literature. With the invention of the printing press by Johannes Gutenberg in the 15th century, the mass production of books became possible, marking a revolutionary leap forward in the dissemination of information.',
              'Typography, as a distinct discipline, emerged during the Renaissance, characterized by the artistic design and arrangement of typefaces. Printing houses in cities like Venice and Paris played crucial roles in standardizing fonts and styles.',
              'The Industrial Revolution brought about mechanized typesetting, further streamlining the printing process. The 19th and 20th centuries witnessed the rise of influential typographers and the advent of new printing technologies, culminating in the digital era, where fonts and styles could be manipulated with unprecedented ease.',
              'In the contemporary landscape, the digital age has ushered in a new chapter in the history of writing and typography. The advent of computers and the internet has transformed the way we create, share, and consume written content. The accessibility of word processors, graphic design software, and online platforms has empowered individuals to become authors, designers, and publishers in their own right. Social media platforms, blogs, and websites have become the canvases for this digital expression, enabling a global exchange of ideas at an unprecedented pace. As we navigate the intricacies of this digital frontier, it becomes evident that the journey of writing and typography is far from over. The ongoing developments in artificial intelligence, augmented reality, and immersive technologies promise to redefine the landscape once again, presenting exciting possibilities for the future of human communication and creative expression. In essence, the history of writing and typography is an ever-unfolding saga, a testament to humanity\'s ability to adapt, innovate, and continually reshape the ways in which we connect through the written word.',
              'The history of writing and typography serves as a testament to human ingenuity and the enduring quest for effective communication. From the earliest symbols etched on cave walls to the sophisticated digital fonts of today, each epoch has contributed to the evolution of a dynamic and expressive means of sharing our thoughts and ideas.'],
    # runes
    'tone2': ['Runes, the ancient symbols of mystery and power, hold a unique place in the history of human communication and spiritual practices. Originating from Germanic and Nordic cultures, runes have transcended their original utilitarian purposes to become enigmatic symbols laden with cultural significance and esoteric meanings.',
              'The earliest runic inscriptions date back to the 2nd century CE in what is now Denmark and Germany. These early runes were likely influenced by the Latin alphabet, but they quickly evolved into a distinct system with angular and straight lines to accommodate the materials used for inscriptions, such as wood, bone, and stone.',
              'Each runic symbol, known as a "rune," carried not only a phonetic value but also a deeper symbolic meaning. The runic alphabet, known as the "Futhark" after its first six letters, was divided into three sets of eight runes each. These groupings, or "aetts," were associated with specific deities and had different magical and divinatory properties.',
              'Runes played a crucial role in the spiritual and religious practices of the Norse and Germanic peoples. They were often inscribed on personal items, weapons, and runestones as a means of invoking protection or seeking guidance from the divine. The runic alphabet was believed to possess a connection to the mystical forces of the universe, making it a powerful tool for communication with the spiritual realm.',
              'The runic tradition also found expression in divination practices, known as "rune casting" or "rune reading." Practitioners would cast or draw runes onto a surface and interpret their positions and relationships to gain insights into the future or seek answers to specific questions. This divinatory aspect added a layer of mysticism to the runic system, making it a revered tool for those seeking guidance.',
              'With the spread of Viking culture through trade, exploration, and conquest, runes left their indelible mark on various regions of Europe. Inscriptions have been found on artifacts ranging from weapons to gravestones, providing glimpses into the lives, beliefs, and aspirations of the people who used them.',
              'The Christianization of Scandinavia led to a decline in the use of runes for official and public inscriptions. However, the runic tradition persisted in more private and esoteric settings, with runic symbols appearing in magical grimoires and folklore.',
              'In the modern era, runes have experienced a resurgence of interest among those exploring esoteric and neo-pagan practices. The runic alphabet is often used for divination, meditation, and as a form of personal symbolism. Contemporary runemasters and enthusiasts study the historical context and meanings associated with each rune to preserve and revive this ancient tradition.',
              'In the contemporary world, the revival of interest in runes extends beyond spiritual or mystical circles. Scholars, linguists, and historians delve into runic inscriptions to unlock the secrets of the past and gain insights into the languages, cultures, and societies that utilized this unique writing system. The study of runes has become an interdisciplinary endeavor, combining linguistics, archaeology, and anthropology to paint a richer picture of the people who once wielded these symbols. As we unravel more of the mysteries hidden within runic inscriptions, we not only deepen our understanding of ancient civilizations but also highlight the enduring allure of runes as a bridge between the tangible and the mystical, connecting us to the roots of human expression and spirituality. In this way, the fascination with runes transcends individual practices and becomes a shared journey of discovery, fostering a greater appreciation for the profound cultural legacy embedded in these ancient symbols.',
              'Runes represent a fascinating chapter in the history of writing and symbolic communication. Originating as a utilitarian script, runes evolved into a profound and mystical system deeply intertwined with the spiritual beliefs and practices of the Norse and Germanic peoples. Today, runes continue to captivate the imagination of those drawn to the ancient mysteries encoded within these enigmatic symbols.'],
    # typography - visual effect
    'tone3': ['Typography, the art and technique of arranging type, has evolved into a powerful design element that can significantly impact the visual appeal and effectiveness of various forms of communication. One of the key components of typography is the selection and use of fonts. Fonts, or typefaces, play a crucial role in conveying a message, setting a tone, and enhancing the overall visual experience.',
              'The choice of fonts goes beyond mere legibility; it involves a careful consideration of the intended message and the target audience. Serif fonts, with their elegant and traditional look, often convey a sense of formality and authority, making them suitable for documents like resumes or academic papers. On the other hand, sans-serif fonts are more modern and clean, making them a popular choice for websites and digital interfaces.',
              'Font size is another crucial factor in visual communication. A well-balanced hierarchy of font sizes helps guide the reader\'s attention, emphasizing key points and creating a more engaging reading experience. Headings and subheadings with larger font sizes can break up content, making it more scannable and digestible.',
              'The spacing between letters, known as kerning, and the spacing between lines, known as leading, contribute significantly to the overall readability and aesthetic appeal of a text. Properly adjusted kerning ensures that letters harmonize with each other, while appropriate leading prevents text from feeling cramped or scattered.',
              'Bold, italics, and underline are styling options that can add emphasis and visual interest to specific words or phrases. When used judiciously, these formatting choices can guide the reader\'s attention and highlight essential information. However, overusing these styles can lead to visual clutter and reduce their effectiveness.',
              'Color can be integrated with fonts to create a visually striking and cohesive design. The right color palette, when combined with appropriate fonts, can evoke specific emotions and reinforce the intended message. Contrast between text and background colors is essential for ensuring readability and accessibility.',
              'Typography plays a crucial role in branding and logo design. Unique and well-chosen fonts can help a brand stand out, communicate its personality, and establish a memorable identity. Consistency in font usage across various brand materials fosters a cohesive and recognizable visual language.',
              'Responsive design in the digital age has heightened the importance of choosing web-safe fonts that render consistently across different devices and browsers. Web fonts, such as Google Fonts or Adobe Typekit, offer a wide range of options for designers to enhance the visual appeal of websites while ensuring a consistent user experience.',
              'Experimental or decorative fonts can be used to inject creativity and personality into design projects. However, it\'s crucial to strike a balance between innovation and readability. While these fonts can be attention-grabbing, they should not compromise the clarity of the message.',
              'The visual use of fonts is a nuanced art that extends far beyond the simple act of choosing typefaces. Typography is a dynamic tool that designers wield to convey meaning, evoke emotions, and create a lasting impression. By understanding the principles of font selection, sizing, spacing, and styling, designers can harness the full potential of typography to elevate the visual impact of their creations.'],
    # visual use of colours
    'tone4': ['Colors are a fundamental aspect of visual communication, influencing emotions, perceptions, and overall aesthetics. The strategic use of colors can transform a design, evoke specific moods, and enhance the impact of any visual project. In this exploration of the visual use of colors, we delve into the principles that guide designers in creating harmonious and visually appealing compositions.',
              'Understanding the color wheel is a foundational step in utilizing colors effectively. Primary, secondary, and tertiary colors form the basis for creating color schemes that range from monochromatic elegance to vibrant complementary contrasts. Designers often leverage these color relationships to establish visual hierarchy and convey a cohesive message.',
              'The psychological impact of colors is a crucial consideration. Warm colors like reds and yellows evoke energy and passion, while cool colors such as blues and greens instill a sense of calm and tranquility. Designers must align the chosen color palette with the intended emotions and messages to create a resonant visual experience.',
              'Color theory extends beyond mere aesthetics; it plays a pivotal role in user experience and accessibility. High contrast between text and background colors enhances readability, while careful consideration of color combinations ensures inclusivity for individuals with visual impairments. Striking the right balance between creativity and usability is paramount.',
              'Cultural and contextual factors significantly influence the perception of colors. Red, for instance, can symbolize luck and prosperity in some cultures but signify danger in others. Designers operating on a global scale must be mindful of cultural nuances to ensure that their color choices resonate positively across diverse audiences.',
              'Monochromatic color schemes, built around variations of a single hue, can create a sophisticated and unified visual language. This approach allows designers to explore subtle nuances within a specific color range, providing depth and interest without overwhelming the viewer with too much diversity.',
              'Complementary colors, positioned opposite each other on the color wheel, create dynamic visual contrasts. When used judiciously, this pairing can draw attention to specific elements and infuse energy into a design. However, excessive use of complementary colors can be visually overwhelming and should be approached with caution.',
              'Analogous color schemes, comprising hues that are adjacent on the color wheel, offer a harmonious and cohesive look. This approach is often employed in nature-inspired designs or those seeking a serene, unified feel. Analogous colors work well together, creating a seamless visual flow throughout the composition.',
              'The concept of color psychology extends to branding and marketing, where specific colors are chosen to evoke desired consumer reactions. For instance, blue is often associated with trust and reliability, making it a popular choice for corporate branding, while vibrant and bold colors may be employed to convey innovation and excitement.',
              'The visual use of colors is a multifaceted art that requires a nuanced understanding of color theory, psychology, and cultural context. Designers who master the interplay of colors unlock the potential to create visually compelling, emotionally resonant, and memorable compositions. Whether aiming for a harmonious blend or a striking contrast, the thoughtful application of colors elevates design beyond mere aesthetics, leaving a lasting impression on the viewer.'],
    # lorem ipsum
    'tone5': ['Lorem Ipsum, a seemingly nonsensical and scrambled arrangement of Latin words, has become a ubiquitous presence in the world of design and typesetting. Originating from a work by Cicero, this placeholder text has served as the industry standard for centuries, providing a neutral and non-distracting way to present visual elements during the design process.',
              'The phrase "Lorem Ipsum" itself has intriguing roots, derived from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil), a philosophical work by Cicero. However, the Lorem Ipsum we commonly encounter in design is not an accurate reproduction of the original text, having undergone various alterations and adaptations over time.',
              'Lorem Ipsum\'s widespread use can be attributed to its ability to mimic the distribution of letters and words in English, making it an effective placeholder for designers and developers. Its nonsensical nature ensures that the focus remains on the visual aspects of a layout rather than on the content itself during the early stages of design.',
              'The intentional gibberish of Lorem Ipsum helps prevent distraction and bias during the review process. By using a language that is unfamiliar to most, clients and stakeholders can evaluate a design\'s layout, font choices, and overall composition without being influenced by the meaning or message of the text.',
              'While Lorem Ipsum has been the go-to placeholder text for centuries, some argue that its overuse has led to a lack of creativity in the design process. In recent years, there has been a growing movement to explore alternative placeholder texts or even incorporate real content during the early stages of design to ensure a more authentic representation of the final product.',
              'Lorem Ipsum has not only found a home in print and web design but has also made its way into pop culture. Its presence in templates and design software has made it a recognizable symbol for the design industry, with memes and jokes often poking fun at its widespread use and seemingly endless repetition.',
              'Despite its popularity, Lorem Ipsum has faced criticism for its lack of cultural sensitivity. As a Latin-derived text, it may not be suitable for all audiences or projects, especially those aiming for a global reach. Some designers advocate for using placeholder text that is more inclusive and reflects the diverse linguistic landscape of the modern world.',
              'The prevalence of Lorem Ipsum in the digital age has led to the creation of Lorem Ipsum generators, online tools that produce custom Lorem Ipsum-style text based on user input. These generators allow designers to tailor the placeholder text to better suit their projects, adding an element of customization to an otherwise standardized practice.',
              'As design trends evolve and the industry continues to embrace diversity and inclusivity, the role of Lorem Ipsum may undergo further scrutiny. Designers are encouraged to explore alternative methods of content representation that align with contemporary values while still serving the practical purpose of allowing for a distraction-free evaluation of design elements.',
              'In conclusion, Lorem Ipsum stands as a curious and enduring aspect of design history. From its ancient origins to its modern applications, this placeholder text has played a vital role in the creative process. While its use remains prevalent, designers are urged to consider alternatives that better align with evolving design practices and values, ensuring a more thoughtful and inclusive approach to content representation during the early stages of visual creation.'],
    # english gibberish - Dreamscript
    'tone6': ['Bicycle dreams pedal through marshmallow meadows, where kaleidoscopic rainbows harmonize with luminescent constellations. Adventure whispers through enchanted firefly labyrinths, as acrobatic giraffes somersault in a pillow of tranquility.',
              'Umbrella symphonies twirl in a bonfire of tangerine dreams, where dragonflies serenade zephyrs of serendipity. Polka dot galaxies giggle with harmonious whispers, creating a meadow of meandering wonderlands.',
              'Melodic cocooned unicorns ride skateboards through quasar bonfires, where cupcake constellations echo in a whimsical carousel of kaleidoscopic laughter. Symphony meadows dance with luminescent echoes.',
              'Cacophonies of marshmallow harmonicas serenade cosmic trampolines, as meandering bicycles navigate luminescent constellations. Serendipitous rainbows cascade through a meadow of whimsy and wonder',
              'Gigantic pillow whispers twirl in a symphony of firefly constellations, where harmonious daydreams serenade polychromatic dreams. Quasar echoes bounce off tangerine meadows in a bonfire of cosmic laughter.',
              'Adventure serenades luminescent giraffes in a kaleidoscope of luminescent zephyrs, as marshmallow constellations giggle with rhythmic daydreams. Galactic symphonies resonate through a meadow of harmonious echoes.',
              'Enchanted bicycles navigate through cosmic whirlwinds, where serendipitous dragonflies somersault in a bonfire of tangerine dreams. Symphony meadows harmonize with luminescent constellations in a polychromatic wonderland.',
              'Pillow symphonies resonate with rhythmic whispers, as quasar constellations twirl in a bonfire of cupcake dreams. Zephyrs of kaleidoscopic laughter echo through luminescent meadows of enchantment.',
              'Giggle rainbows cascade through luminescent meadows, as acrobatic constellations somersault in a cosmic whirlwind. Harmonious whispers serenade quasar unicorns in a symphony of rhythmic dreams.',
              'Majestic unicorns ride skateboards through marshmallow meadows, where rhythmic daydreams harmonize with luminescent constellations. Quasar echoes bounce off enchanted bicycles, creating a pillow of tangerine dreams.'],
}

def generate(event):
    # Assign tone type
    tone_type = document.querySelector("#flavour").value  # Get the value of the selected option

    # Assign paragraph number
    paragraph_number = int(document.querySelector("#paragraph").value)  # Convert the value to an integer

    # Get the list of text items based on user input
    selected_texts = tones.get(tone_type, [])[:paragraph_number]  # Use .get() to handle potential key errors

    # Output the selected text items
    output_box = document.querySelector("#output")
    output_box.innerText = "\n".join(selected_texts)  # Join paragraphs with newline characters

# Attach the 'generate' function to the button click event
generate_button = document.querySelector("#generateButton")
generate_button.addEventListener("click", generate)

