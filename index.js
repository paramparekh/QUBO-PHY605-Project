import Reveal from "reveal.js";
import RevealMath from "reveal.js/plugin/math";
import 'reveal.js/reveal.css';
import 'reveal.js/theme/white.css';

let deck = new Reveal({
    plugins: [ RevealMath.MathJax4 ],
    
});

deck.initialize({
    history: true,
    center: true,
    controls: false,
    margin: 0.2
});