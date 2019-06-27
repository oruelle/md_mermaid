# md_mermaid
mermaid extension for Python-Markdown to add support for mermaid graph inside markdown file

## Installation

* pip (only python version >=3.x) :

~~~shell
pip install markdown
pip install md-mermaid
~~~

## Usage

In your python script :

~~~python
import markdown

text = """
# Title

Some text.

​~~~mermaid
graph TB
A --> B
B --> C
​~~~

Some other text.

​~~~mermaid
graph TB
D --> E
E --> F
​~~~
"""

html = markdown.markdown(text, extensions=['md_mermaid'])

print(html)
~~~

Output will result in :

~~~html
<h1>Title</h1>
<p>Some text.</p>
<div class="mermaid">
graph TB
A --> B
B --> C
</div>

<p>Some other text.</p>
<div class="mermaid">
graph TB
D --> E
E --> F
</div>

<script>mermaid.initialize({startOnLoad:true});</script>

~~~

The `<script>...</script>` line appears only once even if there are several graphs in the file.

> Note that the extension name have a '_' not a '-'.

> Attention : don't forget to include in your output html project the two following mermaid files :
>
> * mermaid.css (optional, can be customised)
> * mermaid.min.js (can be download here [here](https://unpkg.com/mermaid@8.1.0/dist/)) 