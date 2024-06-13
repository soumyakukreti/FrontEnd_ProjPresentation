from rxconfig import config
import reflex as rx
from .states import State
from .pages import about, results, generated 

links = [
    rx.link("Home", href="http://localhost:3000"),
    rx.link("GAN Training Results", href="http://localhost:3000/about"),
    rx.link("Results", href="http://localhost:3000/results"),
    rx.link("Generated", href="http://localhost:3000/generated"),


]

def index() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
            "Data Augmentation using GANs: Generating Synthetic Image Data",
            color="#756AEE",
            font_weight="bold",
            font_size="80px",
            text_align="center",
            ),
            rx.flex(
                rx.box(
                    rx.text("Successful training of convolutional neural networks (CNNs) necessitates a significant quantity of data. Data augmentation techniques enhance the generalizability of neural networks by utilizing existing training data more efficiently. Generative Adversarial Networks (GANs) have been employed to generate novel data and enhance the performance of CNNs. We demonstrate that the proposed GAN can effectively augment data and improve classification accuracy. Additionally, we compare CNN models trained on limited data, a substantial amount of data, and augmented data combined with original data. Our results reveal that our GAN-based augmentation method achieves nearly the same Mean Average Precision (MAP) as the model trained on a substantial amount of data."),
                    border_radius="15px",
                    border_width="thick",
                    padding="1em",
                    border_color="#756AEE",
                    font_size="0.7em",
                    width="50%",
                    
                ),
                rx.spacer(padding="1.0rem"),
                rx.image(
                    src="structure.jpg",
                    width="50%",
                    height="50%",
                    #padding="0.5em",
                    flex="1 1 auto",
                    border_radius="0.5rem",
                    
                ),
                # Size
                padding="2.0rem",

            ),
            # rx.button(
            # "Test Model",
            # border_radius="1em",
            # box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
            # background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            # box_sizing="border-box",
            # color="white",
            # on_click = State.make,
            # _hover={
            #     "opacity": 0.85,
            #     },
            # ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),

        rx.center(
            rx.flex(
                *links,
                # Size
                max_width="1280px",
                width="clamp(288px, 80%, 640px)",
                height="clamp(32px, 50%, 256px)",
                # Flex
                gap="1.0rem",
                padding="1.0rem",
                align_items="center",
                justify="space-evenly",
                # Background
                border_radius="256px",
                backdrop_filter="blur(16px)",
                background_color="rgba(255, 255, 255, 0.15)",
                # Font
                font_weight="600",
                font_size="clamp(16px, 2.5svh, 256px)",
                
            ),
            
        #rx.color_mode_button(rx.color_mode_icon(), float="right"),
        # Position
        top="0.0",
        z_index="5",
        margin="0.0",
        padding="0.0",
        position="fixed",
        # Size
        width="100svw",
        height="12.5svh",
        # Config
        border_radius="1em",
        box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
        background_color="#756AEE",
    
    ),
         
)


# Add state and page to the app.
app = rx.App(state=State)

app.add_page(index)
app.add_page(about)
app.add_page(results)
app.add_page(generated)

app.compile()
