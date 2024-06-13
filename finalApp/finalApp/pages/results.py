import reflex as rx


links = [
    rx.link("Home", href="http://localhost:3000"),
    rx.link("GAN Training Results", href="http://localhost:3000/about"),
    rx.link("Results", href="http://localhost:3000/results"),
    rx.link("Generated", href="http://localhost:3000/generated"),


]

def results() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading("Our Results", font_size="2em", padding_top="10%"),
            rx.flex(
                rx.box(
                    rx.heading("Model Trained on 100 Images",
                               background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                               background_clip="text",
                               padding_bottom="0.5em",
                               ),
                    rx.text("This Model was trained on a dataset of 100 images. All the 100 images were training images and validations and test images are not included in this.", 
                            font_size="0.9em",
                            padding_bottom="0.5em"
                            ),
                     rx.heading("Average Precision: 71.85%",
                               background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                               background_clip="text",
                               padding_bottom="0.5em",
                               font_size="0.9em",
                            ),
                    rx.vstack(
                        rx.image(
                            src="100results.png",
                            width="100%",
                            height="100%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),
                        rx.image(
                            src="100val.png",
                            width="80%",
                            height="80%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),
                    ),
                    border_radius="15px",
                    border_width="thick",
                    padding="1em",
                    border_color="#756AEE",
                    font_size="0.7em",
                    width="50%",
                ),

                rx.spacer(padding="1.0rem"),

                rx.box(
                    rx.heading("Model Trained on 600 Images",
                               background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                               background_clip="text",
                               padding_bottom="0.5em",
                               ),
                    rx.text("This Model was trained on a dataset of 600 images. All the 600 images were training images and validations and test images are not included in this.", 
                            font_size="0.9em",
                            padding_bottom="0.5em"
                            ),
                    rx.heading("Average Precision: 91.87%",
                               background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                               background_clip="text",
                               padding_bottom="0.5em",
                               font_size="0.9em",
                            ),
                    rx.vstack(
                        rx.image(
                            src="600results.png",
                            width="100%",
                            height="100%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),
                        rx.image(
                            src="600val.png",
                            width="80%",
                            height="80%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),
                    ),
                    border_radius="15px",
                    border_width="thick",
                    padding="1em",
                    border_color="#756AEE",
                    font_size="0.7em",
                    width="50%",
                ),
            ),


                rx.box(
                    rx.heading("Model Trained on Augumented Images",
                               background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                               background_clip="text",
                               padding_bottom="0.5em",
                               ),
                    rx.text("This Model was trained on a dataset of 200 synthetic images mixed with 400 real images. All the 600 images were training images and validations and test images are not included in this.", 
                            font_size="0.9em",
                            padding_bottom="0.5em"
                            ),
                     rx.heading("Average Precision: 90.62%",
                               background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                               background_clip="text",
                               padding_bottom="0.5em",
                               font_size="0.9em",
                            ),
                    rx.vstack(
                        rx.image(
                            src="ganresults.png",
                            width="100%",
                            height="100%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),
                        rx.image(
                            src="Ganval.jpg",
                            width="80%",
                            height="80%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),
                    ),
                    border_radius="15px",
                    border_width="thick",
                    padding="1em",
                    border_color="#756AEE",
                    font_size="0.7em",
                    width="50%",
                ),


            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
            padding = "1.0rem",

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