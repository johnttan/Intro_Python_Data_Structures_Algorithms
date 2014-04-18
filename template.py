template = """<!DOCTYPE html>
<html>
  <head>
    <title>Doc Index</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <link rel="stylesheet" media="all" href="central.css" />
    <script type="text/javascript" src="jquery-1.8.0-min.js"></script>
    <script type="text/javascript" src="central.js"></script>
  </head>
  <body>
    <div id="container">
      <div id="background"></div>
      <table cellpadding="0" cellspacing="0">
        <tbody>
          <tr>
            <td class="docs">
              
                <h1>Doc Index</h1>
              
              
              <div id="index">
                <input type="text" class="search" placeholder="Search..." />
                <ul>
                
                  """

template2 = """

                
                </ul>
                <p class="empty" style="display:none;">No match found.</p>
              </div>
            </td>
            <td class="readme">

            </th>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html> 
"""