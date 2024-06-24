text = '''
<html>
    <body bgcolor="grey">
        <h1>Hello World !</h1>
        <table width=100%>
            <tr>
                <td bgcolor="orange">
                    Teste de bgcolor
                </td>
            </tr>
        </table>
    </body>
</html>
'''

file = open("sample.html","w")
file.write(text)
file.close()