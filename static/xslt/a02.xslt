<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/root">

<html>
	<body>
		<h2>Reed Courses</h2>
		<table border="1">
			<tr>
				<th>Subject</th>
				<th>Title</th>
			</tr>
			<xsl:for-each select="course">
				<tr>
					<td><xsl:value-of select="subj"/></td>
					<td><xsl:value-of select="title"/></td>
				</tr>
			</xsl:for-each>
		</table>
	</body>
</html>
</xsl:template>

</xsl:stylesheet>
