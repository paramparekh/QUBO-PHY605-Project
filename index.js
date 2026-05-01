import Reveal from "reveal.js";
import RevealMath from "reveal.js/plugin/math";
import 'reveal.js/reveal.css';
import 'reveal.js/theme/black.css';

let deck = new Reveal({
    plugins: [ RevealMath ],
    
});

deck.initialize({
    history: true,
    center: false,
    controls: false
});