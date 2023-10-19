const home = document.querySelector('.main-container');
const btnHome1 = document.querySelector('#btn-home1');
const btnHome2 = document.querySelector('#btn-home2');
const btnHome3 = document.querySelector('#btn-home3');
const cursor1 = document.querySelector('.cursor1')
const cursor2 = document.querySelector('.cursor2')
const cursor3 = document.querySelector('.cursor3')
const Header = document.querySelector('header');
const footer = document.querySelector('footer');

home.addEventListener('mousemove',(e) => {
    cursor1.style.top = (e.pageY - 100) + "px"
    cursor1.style.left = (e.pageX - 100) + "px"
    
    cursor2.style.top = (e.pageY - 150) + "px"
    cursor2.style.left = (e.pageX - 150) + "px"
    
    cursor3.style.top = (e.pageY - 200) + "px"
    cursor3.style.left = (e.pageX - 200) + "px"
})

btnHome1.addEventListener('mouseover',(e) =>{
    cursor1.style.width = "10px"
    cursor1.style.height = "10px"
    
    cursor2.style.width = "10px"
    cursor2.style.height = "10px"
    
    cursor3.style.width = "10px"
    cursor3.style.height = "10px"
    
    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 5) + "px"
        cursor1.style.left = (e.pageX - 5) + "px"
        
        cursor2.style.top = (e.pageY - 5) + "px"
        cursor2.style.left = (e.pageX - 5) + "px"
        
        cursor3.style.top = (e.pageY - 5) + "px"
        cursor3.style.left = (e.pageX - 5) + "px"
    })
    
    cursor1.style.transition = "200ms"
    cursor2.style.transition = "200ms"
    cursor3.style.transition = "200ms"
})

btnHome1.addEventListener('mouseout',(e) =>{
    cursor1.style.width = "200px"
    cursor1.style.height = "200px"
    
    cursor2.style.width = "300px"
    cursor2.style.height = "300px"
    
    cursor3.style.width = "400px"
    cursor3.style.height = "400px"

    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 100) + "px"
        cursor1.style.left = (e.pageX - 100) + "px"
        
        cursor2.style.top = (e.pageY - 150) + "px"
        cursor2.style.left = (e.pageX - 150) + "px"
        
        cursor3.style.top = (e.pageY - 200) + "px"
        cursor3.style.left = (e.pageX - 200) + "px"
    })

   cursor1.style.transitionProperty = 'width'
   cursor1.style.transitionDuration = '200ms'
   cursor2.style.transitionProperty = 'width'
   cursor2.style.transitionDuration = '200ms'
   cursor3.style.transitionProperty = 'width'
   cursor3.style.transitionDuration = '200ms'
})

btnHome2.addEventListener('mouseover',(e) =>{
    cursor1.style.width = "10px"
    cursor1.style.height = "10px"
    
    cursor2.style.width = "10px"
    cursor2.style.height = "10px"
    
    cursor3.style.width = "10px"
    cursor3.style.height = "10px"
    
    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 5) + "px"
        cursor1.style.left = (e.pageX - 5) + "px"
        
        cursor2.style.top = (e.pageY - 5) + "px"
        cursor2.style.left = (e.pageX - 5) + "px"
        
        cursor3.style.top = (e.pageY - 5) + "px"
        cursor3.style.left = (e.pageX - 5) + "px"
    })
    
    cursor1.style.transition = "200ms"
    cursor2.style.transition = "200ms"
    cursor3.style.transition = "200ms"
})

btnHome2.addEventListener('mouseout',(e) =>{
    cursor1.style.width = "200px"
    cursor1.style.height = "200px"
    
    cursor2.style.width = "300px"
    cursor2.style.height = "300px"
    
    cursor3.style.width = "400px"
    cursor3.style.height = "400px"

    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 100) + "px"
        cursor1.style.left = (e.pageX - 100) + "px"
        
        cursor2.style.top = (e.pageY - 150) + "px"
        cursor2.style.left = (e.pageX - 150) + "px"
        
        cursor3.style.top = (e.pageY - 200) + "px"
        cursor3.style.left = (e.pageX - 200) + "px"
    })

   cursor1.style.transitionProperty = 'width'
   cursor1.style.transitionDuration = '200ms'
   cursor2.style.transitionProperty = 'width'
   cursor2.style.transitionDuration = '200ms'
   cursor3.style.transitionProperty = 'width'
   cursor3.style.transitionDuration = '200ms'
})

btnHome3.addEventListener('mouseover',(e) =>{
    cursor1.style.width = "10px"
    cursor1.style.height = "10px"
    
    cursor2.style.width = "10px"
    cursor2.style.height = "10px"
    
    cursor3.style.width = "10px"
    cursor3.style.height = "10px"
    
    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 5) + "px"
        cursor1.style.left = (e.pageX - 5) + "px"
        
        cursor2.style.top = (e.pageY - 5) + "px"
        cursor2.style.left = (e.pageX - 5) + "px"
        
        cursor3.style.top = (e.pageY - 5) + "px"
        cursor3.style.left = (e.pageX - 5) + "px"
    })
    
    cursor1.style.transition = "200ms"
    cursor2.style.transition = "200ms"
    cursor3.style.transition = "200ms"
})

btnHome3.addEventListener('mouseout',(e) =>{
    cursor1.style.width = "200px"
    cursor1.style.height = "200px"
    
    cursor2.style.width = "300px"
    cursor2.style.height = "300px"
    
    cursor3.style.width = "400px"
    cursor3.style.height = "400px"

    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 100) + "px"
        cursor1.style.left = (e.pageX - 100) + "px"
        
        cursor2.style.top = (e.pageY - 150) + "px"
        cursor2.style.left = (e.pageX - 150) + "px"
        
        cursor3.style.top = (e.pageY - 200) + "px"
        cursor3.style.left = (e.pageX - 200) + "px"
    })

   cursor1.style.transitionProperty = 'width'
   cursor1.style.transitionDuration = '200ms'
   cursor2.style.transitionProperty = 'width'
   cursor2.style.transitionDuration = '200ms'
   cursor3.style.transitionProperty = 'width'
   cursor3.style.transitionDuration = '200ms'
})

Header.addEventListener('mouseover',(e) =>{
    cursor1.style.width = "10px"
    cursor1.style.height = "10px"
    
    cursor2.style.width = "10px"
    cursor2.style.height = "10px"
    
    cursor3.style.width = "10px"
    cursor3.style.height = "10px"
    
    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 5) + "px"
        cursor1.style.left = (e.pageX - 5) + "px"
        
        cursor2.style.top = (e.pageY - 5) + "px"
        cursor2.style.left = (e.pageX - 5) + "px"
        
        cursor3.style.top = (e.pageY - 5) + "px"
        cursor3.style.left = (e.pageX - 5) + "px"
    })
    
    cursor1.style.transition = "200ms"
    cursor2.style.transition = "200ms"
    cursor3.style.transition = "200ms"
})

Header.addEventListener('mouseout',(e) =>{
    cursor1.style.width = "200px"
    cursor1.style.height = "200px"
    
    cursor2.style.width = "300px"
    cursor2.style.height = "300px"
    
    cursor3.style.width = "400px"
    cursor3.style.height = "400px"

    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 100) + "px"
        cursor1.style.left = (e.pageX - 100) + "px"
        
        cursor2.style.top = (e.pageY - 150) + "px"
        cursor2.style.left = (e.pageX - 150) + "px"
        
        cursor3.style.top = (e.pageY - 200) + "px"
        cursor3.style.left = (e.pageX - 200) + "px"
    })

   cursor1.style.transitionProperty = 'width'
   cursor1.style.transitionDuration = '200ms'
   cursor2.style.transitionProperty = 'width'
   cursor2.style.transitionDuration = '200ms'
   cursor3.style.transitionProperty = 'width'
   cursor3.style.transitionDuration = '200ms'
})

footer.addEventListener('mouseover',(e) =>{
    cursor1.style.width = "10px"
    cursor1.style.height = "10px"
    
    cursor2.style.width = "10px"
    cursor2.style.height = "10px"
    
    cursor3.style.width = "10px"
    cursor3.style.height = "10px"
    
    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 5) + "px"
        cursor1.style.left = (e.pageX - 5) + "px"
        
        cursor2.style.top = (e.pageY - 5) + "px"
        cursor2.style.left = (e.pageX - 5) + "px"
        
        cursor3.style.top = (e.pageY - 5) + "px"
        cursor3.style.left = (e.pageX - 5) + "px"
    })
    
    cursor1.style.transition = "200ms"
    cursor2.style.transition = "200ms"
    cursor3.style.transition = "200ms"
})

footer.addEventListener('mouseout',(e) =>{
    cursor1.style.width = "200px"
    cursor1.style.height = "200px"
    
    cursor2.style.width = "300px"
    cursor2.style.height = "300px"
    
    cursor3.style.width = "400px"
    cursor3.style.height = "400px"

    home.addEventListener('mousemove',(e) => {
        cursor1.style.top = (e.pageY - 100) + "px"
        cursor1.style.left = (e.pageX - 100) + "px"
        
        cursor2.style.top = (e.pageY - 150) + "px"
        cursor2.style.left = (e.pageX - 150) + "px"
        
        cursor3.style.top = (e.pageY - 200) + "px"
        cursor3.style.left = (e.pageX - 200) + "px"
    })

   cursor1.style.transitionProperty = 'width'
   cursor1.style.transitionDuration = '200ms'
   cursor2.style.transitionProperty = 'width'
   cursor2.style.transitionDuration = '200ms'
   cursor3.style.transitionProperty = 'width'
   cursor3.style.transitionDuration = '200ms'
})