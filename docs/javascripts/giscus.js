// Giscus 评论系统配置
document.addEventListener('DOMContentLoaded', function () {
    // 检查是否需要添加评论系统（排除首页和特殊页面）
    const currentPath = window.location.pathname;
    const excludePaths = ['/', '/404/', '/404.html'];

    if (!excludePaths.some((path) => currentPath.endsWith(path))) {
        // 创建评论容器
        const article = document.querySelector('.md-content__inner');
        if (article) {
            const commentsContainer = document.createElement('div');
            commentsContainer.className = 'giscus-container';
            commentsContainer.id = 'comments';

            // 添加标题
            const title = document.createElement('h2');
            title.textContent = '💬 讨论交流';
            title.style.marginBottom = '1rem';
            commentsContainer.appendChild(title);

            // 创建 Giscus 脚本
            const script = document.createElement('script');
            script.src = 'https://giscus.app/client.js';
            script.setAttribute('data-repo', 'AlexanderJ-Carter/Notebook');
            script.setAttribute('data-repo-id', 'R_kgDONYrGxQ'); // 你需要替换为实际的 repo ID
            script.setAttribute('data-category', 'General');
            script.setAttribute('data-category-id', 'DIC_kwDONYrGxc4Ck8mQ'); // 你需要替换为实际的 category ID
            script.setAttribute('data-mapping', 'pathname');
            script.setAttribute('data-strict', '0');
            script.setAttribute('data-reactions-enabled', '1');
            script.setAttribute('data-emit-metadata', '0');
            script.setAttribute('data-input-position', 'bottom');
            script.setAttribute('data-theme', 'preferred_color_scheme');
            script.setAttribute('data-lang', 'zh-CN');
            script.crossOrigin = 'anonymous';
            script.async = true;

            commentsContainer.appendChild(script);
            article.appendChild(commentsContainer);
        }
    }

    // 主题切换时更新 Giscus 主题
    const themeToggle = document.querySelector('[data-md-component="palette"]');
    if (themeToggle) {
        themeToggle.addEventListener('change', function () {
            const giscusFrame = document.querySelector('iframe.giscus-frame');
            if (giscusFrame) {
                const theme =
                    document.body.getAttribute('data-md-color-scheme') ===
                    'slate'
                        ? 'dark'
                        : 'light';
                giscusFrame.contentWindow.postMessage(
                    { giscus: { setConfig: { theme: theme } } },
                    'https://giscus.app'
                );
            }
        });
    }
});
