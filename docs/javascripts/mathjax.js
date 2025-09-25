window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
    packages: {'[+]': ['ams', 'newcommand', 'configmacros']}
  },
  svg: {
    fontCache: 'global'
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
    renderActions: {
      find_script: [10, function (doc) {
        for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
          const display = !!node.type.match(/; *mode=display/);
          const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display);
          const text = document.createTextNode(math.math);
          node.parentNode.replaceChild(text, node);
        }
      }, '']
    }
  },
  startup: {
    ready: function () {
      MathJax.startup.defaultReady();
      // 页面加载后立即渲染
      MathJax.typesetPromise().then(() => {
        console.log('MathJax initial render complete');
      });
    }
  }
};

// 监听页面变化，确保公式始终渲染
document$.subscribe(() => {
  if (typeof MathJax !== 'undefined' && MathJax.typesetPromise) {
    MathJax.typesetPromise().catch((err) => {
      console.log('MathJax render error:', err);
    });
  }
});

// DOM 内容加载完成后也进行一次渲染
document.addEventListener('DOMContentLoaded', function() {
  if (typeof MathJax !== 'undefined' && MathJax.typesetPromise) {
    setTimeout(() => {
      MathJax.typesetPromise();
    }, 100);
  }
});