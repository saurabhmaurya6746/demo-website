
  // Show/hide button on scroll
  window.onscroll = function() {
    document.getElementById("scrollBtn").style.display = 
      (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) ? "block" : "none";
  };

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  const carousel = document.getElementById('associationCarousel');
  const bsCarousel = new bootstrap.Carousel(carousel, {
    ride: false,
    wrap: false // 🚫 disables looping
  });

