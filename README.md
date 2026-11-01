# 显示器自检 · Display Check

**中文**：一个本地运行、无需联网的显示器检测工具，包含 10 项全屏测试、一份可保存的检测报告，界面支持简体中文与 English。

**English**: A local, offline display checker with 10 full-screen tests and a saveable report. Runs entirely in your browser — no backend, no analytics, nothing uploaded. If it helps, a star on GitHub would mean a lot.

> ⭐ 觉得有用？给个项目 Star / Found this useful? **[Star it on GitHub](https://github.com/Hugeeeeeeee/display-check)** · 完全本地运行、无统计 / fully local, no analytics · MIT 许可 / Licensed under the MIT License.
>
> 仓库 / Repository：<https://github.com/Hugeeeeeeee/display-check>

## 打开 / Open

- 直接双击 `monitor-check.html`（单文件版，推荐发给别人或拷贝到别的电脑）。
- 或者用浏览器打开 `index.html`（开发版，依赖同目录的 `styles.css` 与 `app.js`）。
- 在线版：<https://display-check-10.pages.dev>（本地运行，打开就能用）。

Just open `monitor-check.html` — it also works from `file://`, no installation and no network access required.

建议使用 Chrome / Edge / Safari。进入测试后会自动尝试全屏，也可以按 `F` 手动切换。

## 使用流程

1. 点击首页的 **开始完整检测**，会从第一个未完成项目开始，并开启连续模式。
2. 每项测试看完后按 `P`（正常）或 `X`（异常），连续模式会自动进入下一项。
3. 最后一项标记完成后会生成 **检测报告**，可以看到结论、逐项结果、备注和屏幕信息。
4. 报告支持 **打印 / 保存 PDF** 与 **复制文字摘要**（适合直接粘贴到聊天记录或售后工单），也可随时点右上角报告图标或按 `R` 查看。
5. 结果只保存在本机浏览器，刷新或关闭页面都不会丢失；**备份进度 / 恢复进度** 可导出、导入 JSON，换电脑或换设备时接着测。

想单独回看某一项时，直接点首页卡片即可；单独进入时不会自动跳到下一项。

不确定怎么判断结果时，按 `T`（或 `?`）打开 **判定小抄**，里面是各项测试的判读标准与测试建议。

## 测试内操作

| 测试 | 可用的 HUD 控件 |
| --- | --- |
| 坏点与纯色 | 9 个颜色块，点击直接切换 |
| 色阶与渐变 | 下拉选择灰阶 / 暗部 / 亮部 / RGB 通道，可开 **抖动** 叠加 8bit 噪点 |
| 亮度均匀性 | 底色块 + 网格开关 |
| 锐度与像素 | 黑 / 白背景切换 |
| 响应与拖影 | 速度滑块 + 暂停 / 继续 |
| 刷新与帧同步 | 暂停 / 继续 |
| 伽马校准 | 纯灰滑块 + 一键重置 186 |

每一项都可以按 `M` 或点底部笔形图标写 **备注**（例如「右下角漏光」「中央有亮斑」），备注会显示在首页卡片、报告中，并随文字摘要一起导出。

## 快捷键

| 按键 | 作用 |
| --- | --- |
| `←` `→` | 上一个 / 下一个测试 |
| `空格` | 当前测试的切换动作（换颜色、换通道、暂停等） |
| `G` | 均匀性测试显示网格 |
| `F` | 全屏 / 退出全屏 |
| `P` / `X` | 标记正常 / 异常 |
| `M` | 当前项写备注 |
| `L` | 切换界面语言 / switch language |
| `R` | 打开检测报告 |
| `T` / `?` | 判定小抄与快捷键面板 |
| `Esc` | 退出全屏；再按一次返回首页 / 关闭报告 / 关闭小抄 |
| `1`–`0` | 首页直接打开对应测试 |

触屏操作：测试中 **左右滑动** 切换上/下一项，**双击屏幕** 标记为正常。

## 测试建议

1. 使用显示器原生分辨率，系统缩放设为 100%（若为高 DPI 屏可按系统推荐）。
2. 关闭夜间模式、护眼模式、HDR 以及厂商的色彩增强 / 锐化功能后再测。
3. 坏点、漏光、灰阶测试建议在暗室进行，并让屏幕预热 20–30 分钟。
4. 响应与刷新测试尽量在独立全屏窗口中进行，浏览器后台标签页会限制动画。

## 判定小抄

- **坏点**：纯色下出现常亮白点、彩点或不亮的黑点即为坏点 / 亮点。
- **色阶**：渐变出现明显竖条纹说明色深或伽马处理不佳；开启 **抖动** 后仍然断层才可疑（抖动用于排除浏览器插值造成的假性断层）。
- **灰阶**：黑阶能分辨到 2–3 级、白阶 245–255 有层次即可。
- **均匀性**：四角与中心不应有明显暗角或偏色；轻微差异属正常。
- **漏光**：IPS 轻微角落漏光正常，大面积光晕或泛白可考虑退换。
- **锐度**：1:1 棋盘格不应出现摩尔纹；文字不应发虚或出现明显彩边。
- **拖影**：运动条纹边缘不应有长拖尾、白边或黑边（过冲）。
- **刷新**：实测 Hz 应接近标称值，竖条移动应匀速无跳格。
- **视角**：侧视时颜色不应明显泛白、偏色或丢失细节。
- **伽马**：滑块在 186 附近两侧亮度一致，说明 γ 接近 2.2。

## 语言 / Language

- 界面语言优先读你上次手动选择的值（`localStorage`），没有选择过时按浏览器语言自动判定：`zh*` 用简体中文，其余用 English。
- 切换入口：首页右上角的「中 / EN」分段控件、测试中与报告页右上角的语言按钮、键盘 `L`。切换后当前打开的测试、报告、小抄文案立即更新，不用返回首页。
- 报告文字摘要、备份 JSON、打印页脚也会跟随当前语言；测试画面本身（色块、棋盘格、样张文字）不随语言变化，只有说明文字会变。
- 新增第三种语言只需在 `app.js` 的文案字典里复制一份字典并在 `STRINGS` 登记，渲染逻辑无需修改；字典缺项会回退到中文并显示 `???`，不会出现空白或裸露键名。

## Star

仓库：<https://github.com/Hugeeeeeeee/display-check>（在线试用：<https://display-check-10.pages.dev>）

仓库地址只写在 **一处** —— `app.js` 顶部的 `REPO` 常量（改完必须重新执行 `python3 build.py`，否则 `monitor-check.html` 与 `site/` 里的地址不会更新）：

```js
const REPO = 'Hugeeeeeeee/display-check';   // 不要加 https://
```

它会同时驱动首页的 GitHub 入口、报告页顶部的一次性说明条、报告底部页脚、文字摘要与备份 JSON 里的项目地址。保持占位符 `YOUR_GITHUB_USERNAME` 不动时，这些入口会自动隐藏，不会出现指向不存在页面的链接。说明条只在用户完成一整轮检测并首次打开报告时出现一次，关闭或看过之后记录在 `localStorage`，不再重复打扰；它只是一个普通 `<a target="_blank" rel="noopener noreferrer">` 跳转，不涉及任何统计脚本或外部请求。

## 构建与部署

```bash
python3 build.py
```

会生成：

- `monitor-check.html`：单文件离线版。
- `site/`：可直接上传到 Cloudflare Pages 的静态站点（`index.html`、`404.html`、`_headers`、`robots.txt`、`LICENSE`）。

改完 `index.html` / `styles.css` / `app.js` 或 `build.py` 里的 `_headers` 模板后，必须重新执行一次 `python3 build.py`，否则线上产物与源码不同步。Building also copies the site into `site/` — remember to rebuild before deploying.

## 部署到 Cloudflare Pages

1. 把仓库推到 GitHub，在 Cloudflare Pages 选择 *Connect to Git* 并选中该仓库。
2. 构建设置填 **Framework preset: None**，**Build command** 留空（或写 `python3 build.py`，若平台有 Python），**Output directory** 填 `site`。
   - 如果不想在平台上跑 Python，可以先本地执行 `python3 build.py` 再把 `site/` 一起提交，直接把 Output directory 指向 `site`。
3. 项目名（即域名）填 `display-check-10`，得到 `https://display-check-10.pages.dev`。pages.dev 的项目名**全局唯一**：`display-check`、`monitor-check`、`screen-check` 已被他人占用，若 `display-check-10` 也提示已存在，依次试 `displaycheck10`、`monitor-self-check`，选定后回来同步更新本页顶部与「Star」小节的链接。
4. 后续每次 `git push` 会自动重新部署，几分钟内生效。

`site/_headers` 已配置安全响应头与不缓存 HTML，无需额外设置。站点是纯静态文件，不依赖任何外部资源与网络请求。

*Deployment in short: push to GitHub → Cloudflare Pages → Connect to Git → Framework preset **None**, Build command **empty**, Output directory **`site`**, production branch **`main`**. Every push redeploys automatically; no build step is needed in the cloud because `site/` is committed.*

## 隐私

- 无后端、无统计、无广告、无外部字体与 CDN，所有请求都在本地完成（`connect-src 'none'` 从响应头层面封死了对外连接）。
- 不采集也不上传屏幕参数、标记结果与备注；它们只存在你浏览器的 `localStorage` 里，清空浏览器数据即彻底删除。
- 分享结果靠本地产物：复制文字摘要、打印 / 保存 PDF、导出备份 JSON，内容完全由你掌控。
- 响应头已关闭摄像头 / 定位 / 支付 / 各类传感器权限，发送 `Referrer-Policy: no-referrer`，并用 `frame-ancestors 'none'` 禁止被他人页面嵌入，访问记录不会回传给第三方。
- 项目以匿名作者名义发布（见 `LICENSE`），提交记录使用 GitHub 的 noreply 邮箱，不绑定真实邮箱。
- 对外链接只有一个 GitHub 仓库地址，且只在普通 `<a>` 标签里出现；页面不发起任何 `fetch`／XHR／WebSocket 请求。

*Privacy in short: no backend, no analytics, no ads, no external fonts or CDNs; `connect-src 'none'` blocks outbound requests at the header level. Screen specs, marks and notes never leave your browser — they live in `localStorage` only, and sharing happens through local artefacts (copied summary, printed PDF, exported JSON).*

## 许可

本项目以 MIT 协议开源，可自由使用、修改与分发，详见 [LICENSE](LICENSE)（线上 `/LICENSE` 也可查看）。

Licensed under the MIT License — see [LICENSE](LICENSE).

## 说明

- 刷新率由 `requestAnimationFrame` 估算，结果为浏览器实际呈现的帧率。
- 色域 / HDR 信息来自浏览器的显示能力检测，不代表面板的实验室测量值。
- 标记结果与备注保存在浏览器 `localStorage`，仅本机可见；需要跨设备时使用报告页的 **备份进度 / 恢复进度**。
- 复制文字摘要与备份下载都发生在本地，站点没有访问任何外部服务（`connect-src 'none'`）。
- 报告结论基于人工目视观察，仅作为选购与退换参考。
