import openai 
import streamlit as st  

# Set your OpenAI API key 
openai.api_key = ""


# Helper function 
def generate_text(messages, model="gpt-3.5-turbo", max_tokens=300): 
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=1.0
    )
    return response.choices[0].message["content"].strip()

# Agents
def generate_plot(user_request):
    messages = [
        {"role": "system", "content": "You are a story planner."},
        {"role": "user", "content": f"Create a plot outline for this request: {user_request}"}
    ]
    return generate_text(messages)

def generate_character(plot):
    messages = [
        {"role": "system", "content": "You are a character creator."},
        {"role": "user", "content": f"Based on this plot: '{plot}', create a detailed character description for the hero."}
    ]
    return generate_text(messages)

def generate_setting(plot):
    messages = [
        {"role": "system", "content": "You are a world builder."},
        {"role": "user", "content": f"Based on this plot: '{plot}', describe the story setting."}
    ]
    return generate_text(messages)

def generate_dialogue(character, setting):
    messages = [
        {"role": "system", "content": "You are a dialogue writer."},
        {"role": "user", "content": f"Write the first conversation between the hero {character} and a mysterious guide. The setting is {setting}."}
    ]
    return generate_text(messages)

def generate_emotion(character, plot):
    messages = [
        {"role": "system", "content": "You are an emotional depth creator."},
        {"role": "user", "content": f"Based on the character {character} and the plot '{plot}', create an emotional twist that tests the hero."}
    ]
    return generate_text(messages)

# Full Story
def generate_story(user_request):
    plot = generate_plot(user_request)
    character = generate_character(plot)
    setting = generate_setting(plot)
    dialogue = generate_dialogue(character, setting)
    emotion = generate_emotion(character, plot)

    story = (
        f"### Story Outline:\n{plot}\n\n"
        f"### Character Development:\n{character}\n\n"
        f"### Setting Description:\n{setting}\n\n"
        f"### First Dialogue:\n{dialogue}\n\n"
        f"### Emotional Twist:\n{emotion}\n"
    )
    return story

# Streamlit App
def main():
    st.title("AI Story Generator 🎭")
    st.write("Describe the story you want, and the AI will create it step by step!")

    user_request = st.text_input("Enter your story idea (e.g., 'A detective story set in Mumbai with a twist ending'):")

    if st.button("Generate Story"):
        if user_request.strip():
            with st.spinner("Crafting your story... ✨"):
                story = generate_story(user_request)
            st.markdown(story)
        else:
            st.warning("Please enter a story idea first!")

if __name__ == "__main__":
    main()
