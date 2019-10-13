"""
# Creates a button to toggle code inputs on and off. for Ipynb
# https://wikidocs.net/7055
"""
# print(__doc__)

import IPython.core.display as di
from IPython.core.display import display_html

di.display_html(
    '''
        <script>
          'use strict';
          function code_toggle() {
            let code = $('div.input');
            code.css('display') == 'none' ? code.show() : code.hide();
          }
          $(document).ready(function() {
            $('div.input').hide();
          });
        </script>
        <button onclick="code_toggle()">Toggle Code</button>
    ''',
    raw=True
    )


from IPython.display import display
from IPython.display import HTML
# Example: di.display_html('<h3>%s:</h3>' % str, raw=True)
# This line will hide code by default when the notebook is exported as HTML
di.display_html(
    """
    <script>
      jQuery(
        function() {
          if (jQuery("body.notebook_app").length == 0) {
            jQuery(".input_area").toggle();
            jQuery(".prompt").toggle();
          }
        }
      );
    </script>
    <button onclick="
        jQuery('.input_area').toggle();
        jQuery('.prompt').toggle();
        ">Toggle code</button>
    """
    ,
    raw=True
    )

# This line will add a button to toggle visibility of code blocks,
# for use with the HTML export version




HTML(
    '''
    <script>
    code_show=true;
    function code_toggle() {
     if (code_show){
     $('div.input').hide();
     } else {
     $('div.input').show();
     }
     code_show = !code_show
    }
    $( document ).ready(code_toggle);
    </script>
    '''
    )
