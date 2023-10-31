from jinja2 import Template
import webbrowser

class htmlGenerator:
    def get_dataset_overview():
        pass
    
    
    def generate_report(overview):
        
        # Define your HTML template
        template_str = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="{{ css_file }}">
            <title>Overview Page</title>
        </head>
        <body>
            <div class = "row header">
                <h1 class="page-header">Overview</h1>
            </div>
            
            <div class="overview">
                {% for key, value in overview.items() %}
                    <div class="overview-item">
                        <li>{{ key }}: {{ value }}</li>
                    </div>
                {% endfor %}
            </div>
            
            <div class = "row header">
                <h1 class="page-header"> Dataset Metrics </h1>
            </div>
            
        </body>
        </html>
        """

        # Create a Jinja2 template from the template string
        template = Template(template_str)

        # Render the template with the overview information
        rendered_html = template.render(overview = overview, css_file = "dppa_styles.css")

        # Save the rendered HTML to a file
        with open('overview_page.html', 'w') as f:
            f.write(rendered_html)
            
        # Open the file in a new tab
        webbrowser.open_new_tab('overview_page.html')







        
    