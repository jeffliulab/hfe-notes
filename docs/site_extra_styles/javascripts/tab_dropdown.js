// 顶部标签页悬停下拉预览菜单（支持二级→三级子菜单，三级带链接）
// 此文件由 hooks/generate_dropdown.py 自动生成，请勿手动编辑
// 如需修改 UI 逻辑，请编辑 hooks/tab_dropdown.tpl.js
(function () {
  var tabData = {"ENP111": [{"name": "ENP111总览", "path": "ENP111/", "pages": []}, {"name": "人因导论", "path": "ENP111/human_factors_intro/", "pages": []}, {"name": "人为失误框架", "path": "ENP111/human_error_frameworks/", "pages": []}, {"name": "Swiss Cheese 模型", "path": "ENP111/swiss_cheese/", "pages": []}, {"name": "任务分析", "path": "ENP111/task_analysis/", "pages": []}, {"name": "URRA方法", "path": "ENP111/urra_methods/", "pages": []}, {"name": "Known Problem 与事件树", "path": "ENP111/known_problem_and_event_tree/", "pages": []}, {"name": "ISO 14971", "path": "ENP111/iso_14971/", "pages": []}, {"name": "医疗器械URRA", "path": "ENP111/medical_device_urra/", "pages": []}, {"name": "医疗器械使用错误", "path": "ENP111/medical_device_use_errors/", "pages": []}, {"name": "EpiPen工作簿", "path": "ENP111/epipen_workbook/", "pages": []}], "ENP112": [{"name": "ENP112总览", "path": "ENP112/", "pages": []}, {"name": "课程导论", "path": "ENP112/course_overview/", "pages": []}, {"name": "错误分析方法", "path": "ENP112/error_analysis_methods/", "pages": []}, {"name": "航空与自动化导论", "path": "ENP112/aviation_automation_intro/", "pages": []}, {"name": "CRM", "path": "ENP112/crew_resource_management/", "pages": []}, {"name": "显示与告警", "path": "ENP112/displays_and_alerts/", "pages": []}, {"name": "检查单与程序", "path": "ENP112/checklists_and_procedures/", "pages": []}, {"name": "自动化车辆", "path": "ENP112/automated_vehicles/", "pages": []}, {"name": "注意与监控", "path": "ENP112/attention_and_monitoring/", "pages": []}, {"name": "疲劳与睡眠", "path": "ENP112/fatigue_and_sleep/", "pages": []}, {"name": "压力与决策", "path": "ENP112/stress_and_decision_making/", "pages": []}, {"name": "情境意识", "path": "ENP112/situation_awareness/", "pages": []}, {"name": "空间定向错觉", "path": "ENP112/spatial_disorientation/", "pages": []}, {"name": "Operational Risk", "path": "ENP112/operational_risk/", "pages": []}, {"name": "Cardosi案例", "path": "ENP112/cardosi_case/", "pages": []}, {"name": "F16分析提示", "path": "ENP112/f16_analysis_prompts/", "pages": []}, {"name": "Boeing 737 Max与伦理", "path": "ENP112/boeing_737max_and_ethics/", "pages": []}]};

  if (typeof tabData === "undefined") return;

  function getBase() {
    var host = window.location.hostname;
    if (host === "127.0.0.1" || host === "localhost") return "/";
    var parts = window.location.pathname.split("/").filter(Boolean);
    return parts.length ? "/" + parts[0] + "/" : "/";
  }

  var currentDropdown = null;
  var currentTab = null;
  var currentSubMenu = null;

  function hideAll() {
    if (currentSubMenu) { currentSubMenu.remove(); currentSubMenu = null; }
    if (currentDropdown) { currentDropdown.remove(); currentDropdown = null; currentTab = null; }
  }

  function hideSubMenu() {
    if (currentSubMenu) { currentSubMenu.remove(); currentSubMenu = null; }
  }

  function showSubMenu(itemEl, pages, base, parentRect) {
    hideSubMenu();
    var sub = document.createElement("div");
    sub.className = "tab-dropdown tab-submenu";
    pages.forEach(function (p) {
      var a = document.createElement("a");
      a.className = "tab-dropdown__item";
      a.textContent = p[0];
      a.href = base + p[1];
      sub.appendChild(a);
    });
    var itemRect = itemEl.getBoundingClientRect();
    sub.style.position = "fixed";
    sub.style.top = itemRect.top + "px";
    sub.style.left = parentRect.right + 2 + "px";
    document.body.appendChild(sub);
    currentSubMenu = sub;
  }

  function show(link, sections) {
    if (currentTab === link) return;
    hideAll();
    currentTab = link;
    var base = getBase();
    var rect = link.getBoundingClientRect();
    var el = document.createElement("div");
    el.className = "tab-dropdown";
    sections.forEach(function (sec) {
      var a = document.createElement("a");
      a.className = "tab-dropdown__item";
      a.textContent = sec.name;
      a.href = sec.path ? base + sec.path : (link.getAttribute("href") || link.href);
      if (sec.pages && sec.pages.length > 0) {
        a.classList.add("has-submenu");
        a.addEventListener("mouseenter", function () {
          showSubMenu(a, sec.pages, base, el.getBoundingClientRect());
        });
      } else {
        a.addEventListener("mouseenter", hideSubMenu);
      }
      el.appendChild(a);
    });
    el.style.position = "fixed";
    el.style.top = rect.bottom + "px";
    el.style.left = rect.left + rect.width / 2 + "px";
    el.style.transform = "translateX(-50%)";
    document.body.appendChild(el);
    currentDropdown = el;
  }

  function init() {
    var tabsBar = document.querySelector(".md-tabs");
    if (!tabsBar || tabsBar.getAttribute("data-dd")) return;
    tabsBar.setAttribute("data-dd", "1");

    document.querySelectorAll(".md-tabs__link").forEach(function (link) {
      var text = link.textContent.trim();
      var sections = tabData[text];
      if (!sections) return;
      link.addEventListener("mouseenter", function () { show(link, sections); });
    });

    document.addEventListener("mousemove", function (e) {
      if (!currentDropdown) return;
      var tbr = document.querySelector(".md-tabs").getBoundingClientRect();
      var ddr = currentDropdown.getBoundingClientRect();
      var inTabs = e.clientY >= tbr.top && e.clientY <= tbr.bottom + 4
                   && e.clientX >= tbr.left && e.clientX <= tbr.right;
      var inDd = e.clientY >= ddr.top - 4 && e.clientY <= ddr.bottom
                 && e.clientX >= ddr.left && e.clientX <= ddr.right;
      var inSub = false;
      if (currentSubMenu) {
        var sr = currentSubMenu.getBoundingClientRect();
        inSub = e.clientY >= sr.top && e.clientY <= sr.bottom
                && e.clientX >= sr.left - 4 && e.clientX <= sr.right;
      }
      if (!inTabs && !inDd && !inSub) hideAll();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
  if (typeof document$ !== "undefined") {
    document$.subscribe(function () { init(); });
  }
})();
