HTML:
![alt text](image.png)
Headings:
       <h1></h1>  till <h6></h6>
List:
         <ul> 
             <li> </li> 
         </ul>
         <ol> 
             <li> </li> 
        </ol>
         <dl> <dt> <dd> </dd> </dt> </dl>   

Images:
        <img src="image.png" alt="alt text" width="100" height="100">
Links:
        <a href="url">link text</a>
Tables:
      table, 
        thead,
              tr,
                  th,
        tbody,
             tr,
                td,

Form:
        form,
            input, 
            textarea,
            button,
            select,
            option,
            label,
            fieldset,
            legend
     

CSS:
Type of CSS:
    Inline : <h1 style="color:blue;">This is a Blue Heading</h1>
    Internal : <style> h1 {color:red;} </style>
    External : <link rel="stylesheet" type="text/css" href="styles.css">
Selectors:
    Universal Selector : *{}
    Type Selector : h1{}
    Class Selector : .class{}
    ID Selector : #id{}
    Descendant Selector : h1 p{} i.e. p inside h1, style will be applied to p
    Child Selector : h1 > p{} i.e. p is direct child of h1, style will be applied to p
    Adjacent Sibling Selector : h1 + p{} i.e. p is immediate sibling of h1, style will be applied to p
    Attribute Selector : a[title]{} i.e. a tag with title attribute, style will be applied to a
    Pseudo-classes : a:hover{} i.e. a tag when hovered, style will be applied to a
    Pseudo-elements : p::first-line{} i.e. first line of p tag, style will be applied to p
    Grouping Selector : h1, p{} i.e. style will be applied to both h1 and p
    Combinators : h1 ~ p{} i.e. p tag after h1, style will be applied to p   

Specificity:
    Inline > ID > Class > Type

Responsive Design:
    Media Queries:
        @media not|only mediatype and (expressions) {
            CSS-Code;
        }
    Viewport:
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    Flexbox:
        display: flex;
        flex-direction: row | row-reverse | column | column-reverse;
        justify-content: flex-start | flex-end | center | space-between | space-around;
        align-items: flex-start | flex-end | center | baseline | stretch;
        flex-wrap: nowrap | wrap | wrap-reverse;
        flex-flow: column wrap;
        align-content: flex-start | flex-end | center | space-between | space-around | stretch;
    Grid:
        display: grid;
        grid-template-columns: 100px 100px 100px;
        grid-template-rows: auto;
        grid-column-gap: 10px;
        grid-row-gap: 10px;
        grid-gap: 10px 15px;
        grid-template-areas: "header header header"
                             "main main sidebar"
                             "footer footer footer";
        grid-area: header;
        justify-self: center | start | end | stretch;
        align-self: center | start | end | stretch;
    Bootstrap:
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
        container, container-fluid
        grid system
        margin and padding
        form and button styles
        alert and progress bar styles
        navbar and navs
        modal and dropdown
        carousel and collapse        