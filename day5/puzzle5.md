<!DOCTYPE html>
<html lang="en-us">
<head>
<meta charset="utf-8"/>
<title>Day 5 - Advent of Code 2022</title>
<!--[if lt IE 9]><script src="/static/html5.js"></script><![endif]-->
<link href='//fonts.googleapis.com/css?family=Source+Code+Pro:300&subset=latin,latin-ext' rel='stylesheet' type='text/css'/>
<link rel="stylesheet" type="text/css" href="/static/style.css?30"/>
<link rel="stylesheet alternate" type="text/css" href="/static/highcontrast.css?0" title="High Contrast"/>
<link rel="shortcut icon" href="/favicon.png"/>
<script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
</head><!--




Oh, hello!  Funny seeing you here.

I appreciate your enthusiasm, but you aren't going to find much down here.
There certainly aren't clues to any of the puzzles.  The best surprises don't
even appear in the source until you unlock them for real.

Please be careful with automated requests; I'm not a massive company, and I can
only take so much traffic.  Please be considerate so that everyone gets to play.

If you're curious about how Advent of Code works, it's running on some custom
Perl code. Other than a few integrations (auth, analytics, social media), I
built the whole thing myself, including the design, animations, prose, and all
of the puzzles.

The puzzles are most of the work; preparing a new calendar and a new set of
puzzles each year takes all of my free time for 4-5 months. A lot of effort
went into building this thing - I hope you're enjoying playing it as much as I
enjoyed making it for you!

If you'd like to hang out, I'm @ericwastl on Twitter.

- Eric Wastl


















































-->
<body>
<header><div><h1 class="title-global"><a href="/">Advent of Code</a></h1><nav><ul><li><a href="/2022/about">[About]</a></li><li><a href="/2022/events">[Events]</a></li><li><a href="https://teespring.com/stores/advent-of-code" target="_blank">[Shop]</a></li><li><a href="/2022/settings">[Settings]</a></li><li><a href="/2022/auth/logout">[Log Out]</a></li></ul></nav><div class="user">Daniel Luftspring <span class="star-count">8*</span></div></div><div><h1 class="title-event">&nbsp;&nbsp;&nbsp;<span class="title-event-wrap">sub y{</span><a href="/2022">2022</a><span class="title-event-wrap">}</span></h1><nav><ul><li><a href="/2022">[Calendar]</a></li><li><a href="/2022/support">[AoC++]</a></li><li><a href="/2022/sponsors">[Sponsors]</a></li><li><a href="/2022/leaderboard">[Leaderboard]</a></li><li><a href="/2022/stats">[Stats]</a></li></ul></nav></div></header>

<div id="sidebar">
<div id="sponsor"><div class="quiet">Our <a href="/2022/sponsors">sponsors</a> help make Advent of Code possible:</div><div class="sponsor"><a href="https://www.bjss.com/" target="_blank" onclick="if(ga)ga('send','event','sponsor','sidebar',this.href);" rel="noopener">BJSS</a> - Our people are a team of problem solvers, experienced in evolving technologies and delivering world-class technology solutions.</div></div>
</div><!--/sidebar-->

<main>
<article class="day-desc"><h2>--- Day 5: Supply Stacks ---</h2><p>The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked <em>crates</em>, but because the needed supplies are buried under many other crates, the crates need to be rearranged.</p>
<p>The ship has a <em>giant cargo crane</em> capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.</p>
<p>The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her <em>which</em> crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.</p>
<p>They do, however, have a drawing of the starting stacks of crates <em>and</em> the rearrangement procedure (your puzzle input). For example:</p>
<pre><code>    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
</code></pre>
<p>In this example, there are three stacks of crates. Stack 1 contains two crates: crate <code>Z</code> is on the bottom, and crate <code>N</code> is on top. Stack 2 contains three crates; from bottom to top, they are crates <code>M</code>, <code>C</code>, and <code>D</code>. Finally, stack 3 contains a single crate, <code>P</code>.</p>
<p>Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:</p>
<pre><code>[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
</code></pre>
<p>In the second step, three crates are moved from stack 1 to stack 3. Crates are moved <em>one at a time</em>, so the first crate to be moved (<code>D</code>) ends up below the second and third crates:</p>
<pre><code>        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
</code></pre>
<p>Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved <em>one at a time</em>, crate <code>C</code> ends up below crate <code>M</code>:</p>
<pre><code>        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
</code></pre>
<p>Finally, one crate is moved from stack 1 to stack 2:</p>
<pre><code>        [<em>Z</em>]
        [N]
        [D]
[<em>C</em>] [<em>M</em>] [P]
 1   2   3
</code></pre>
<p>The Elves just need to know <em>which crate will end up on top of each stack</em>; in this example, the top crates are <code>C</code> in stack 1, <code>M</code> in stack 2, and <code>Z</code> in stack 3, so you should combine these together and give the Elves the message <code><em>CMZ</em></code>.</p>
<p><em>After the rearrangement procedure completes, what crate ends up on top of each stack?</em></p>
</article>
<p>To begin, <a href="5/input" target="_blank">get your puzzle input</a>.</p>
<form method="post" action="5/answer"><input type="hidden" name="level" value="1"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=%22Supply+Stacks%22+%2D+Day+5+%2D+Advent+of+Code+2022&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F5&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' && mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=%22Supply+Stacks%22+%2D+Day+5+%2D+Advent+of+Code+2022+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F5'}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
</main>

<!-- ga -->
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');
</script>
<!-- /ga -->
</body>
</html>