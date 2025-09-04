
import gradio as gr
from resume_pipeline import process_resume

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="purple")) as demo:
    gr.Markdown("# 📝 Resume Optimizer (2-page limit)")
    gr.Markdown("Upload your resume (PDF). It will be rewritten and formatted professionally.")

    with gr.Row():
        input_pdf = gr.File(label="📂 Upload Resume (PDF)", file_types=[".pdf"])
        output_pdf = gr.File(label="📥 Download Rewritten Resume", interactive=False)

    run_button = gr.Button(" Rewrite Resume", variant="primary")

    run_button.click(fn=process_resume, inputs=input_pdf, outputs=output_pdf)

if __name__ == "__main__":
    demo.launch()
