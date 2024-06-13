import reflex as rx

links = [
    rx.link("Home", href="http://localhost:3000"),
    rx.link("GAN Training Results", href="http://localhost:3000/about"),
    rx.link("Results", href="http://localhost:3000/results"),
    rx.link("Generated", href="http://localhost:3000/generated"),


]

def about() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading("Traninig Results", font_size="2em", color="#756AEE"),
            rx.box(
                rx.text("Our study utilized a dataset of 30,000 cat face images (64x64) collected from a Kaggle dataset. The DC GAN was trained on this dataset for 5,200 epochs, with a batch size of 256. Our implementation of DC GAN was reliant upon the Tensorflow and Keras library."),
                rx.vstack(
        
                     rx.heading("Generator vs Discriminator Loss for first 1400 epochs",
                            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            padding_bottom="0.5em",
                            font_size="1.3em",
                            padding_top="2em",
                        ),            
                    rx.image(
                            src="1400loss.png",
                            width="70%",
                            height="70%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),

                    rx.heading("Generator vs Discriminator Loss for next 3500 epochs",
                            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            padding_bottom="0.5em",
                            font_size="1.3em",
                            padding_top="2em",
                        ),            
                    rx.image(
                            src="3500loss.jpg",
                            width="70%",
                            height="70%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),
        
                    rx.heading("At Epoch 1",
                            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            padding_bottom="0.5em",
                            font_size="1.3em",
                            padding_top="2em",
                        ),            
                    rx.image(
                            src="image_at_epoch_0001.png",
                            width="70%",
                            height="70%",
                            #padding="0.5em",
                            flex="1 1 auto",
                            border_radius="0.5rem",
                        ),
                    rx.heading("At Epoch 1526",
                            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            padding_bottom="0.5em",
                            font_size="1.3em",
                            padding_top="2em",
                        ), 
                    rx.image(
                        src="image_at_epoch_1526.jpg",
                        width="70%",
                        height="70%",
                        #padding="0.5em",
                        flex="1 1 auto",
                        border_radius="0.5rem",
                    ),

                    rx.heading("At Epoch 2423",
                            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            padding_bottom="0.5em",
                            font_size="1.3em",
                            padding_top="2em",
                        ), 
                    rx.image(
                        src="image_at_epoch_2423.jpg",
                        width="70%",
                        height="70%",
                        #padding="0.5em",
                        flex="1 1 auto",
                        border_radius="0.5rem",
                    ),

                    rx.heading("At Epoch 5201",
                            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            padding_bottom="0.5em",
                            font_size="1.3em",
                            padding_top="2em",
                        ), 
                    rx.image(
                        src="image_at_epoch_5201.jpg",
                        width="70%",
                        height="70%",
                        #padding="0.5em",
                        flex="1 1 auto",
                        border_radius="0.5rem",
                    ),


                    rx.heading("Complete Training Results",
                            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            padding_bottom="0.5em",
                            font_size="1.3em",
                            padding_top="2em",
                        ), 
                    rx.image(
                        src="cats_gan.gif",
                        width="70%",
                        height="70%",
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