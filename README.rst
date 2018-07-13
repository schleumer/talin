talin
=====

Based on Mailgun's Talon, a library to extract message quotations and JUST it, no ML, thanks. It's good for lightweight applications that runs on AWS Lambda or likewise stuff.

No cool text for this fork :disappointed_relieved:

Usage
-----

Here’s how you initialize the library and extract a reply from a text
message:

.. code:: python

    import talin
    from talin import quotations

    talin.init()

    text =  """Reply

    -----Original Message-----

    Quote"""

    reply = quotations.extract_from(text, 'text/plain')
    reply = quotations.extract_from_plain(text)
    # reply == "Reply"

To extract a reply from html:

.. code:: python

    html = """Reply
    <blockquote>

      <div>
        On 11-Apr-2011, at 6:54 PM, Bob &lt;bob@example.com&gt; wrote:
      </div>

      <div>
        Quote
      </div>

    </blockquote>"""

    reply = quotations.extract_from(html, 'text/html')
    reply = quotations.extract_from_html(html)
    # reply == "<html><body><p>Reply</p></body></html>"

Research
--------

The library is inspired by the following research papers and projects:

-  http://www.cs.cmu.edu/~vitor/papers/sigFilePaper_finalversion.pdf
