<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <head>
  <style>
body {background-color: #DECEE7;
font-size:16pt;
}
.low{
color: blue;
}
.medium{
color: red;
}
.high{
color: green;
}
</style>
</head>
  <body>

    <xsl:for-each select="catalog/food">
    <img>
    	<xsl:attribute name="src">
        	<xsl:value-of select="Photo"/>
    	</xsl:attribute>
	</img>
	<br/>
	<p class="{availability}">
    <xsl:value-of select="type"/>
	<xsl:value-of select="Name"/>
    </p>
	
    <br/>
    
    
    </xsl:for-each>

  </body>
  </html>
</xsl:template>

</xsl:stylesheet>