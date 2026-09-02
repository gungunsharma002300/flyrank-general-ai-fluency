document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',()=>{document.body.dataset.lastSection=a.getAttribute('href')})
});
