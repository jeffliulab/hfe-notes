// 顶部标签页悬停下拉预览菜单（支持二级→三级子菜单，三级带链接）
// 此文件由 hooks/generate_dropdown.py 自动生成，请勿手动编辑
// 如需修改 UI 逻辑，请编辑 hooks/tab_dropdown.tpl.js
(function () {
  var tabData = {"HFE基础": [{"name": "HFE基础总览", "path": "HFE_Foundations/", "pages": []}, {"name": "课程导论", "path": "HFE_Foundations/course_overview/", "pages": []}, {"name": "人因导论", "path": "HFE_Foundations/human_factors_intro/", "pages": []}, {"name": "人为失误框架", "path": "HFE_Foundations/human_error_frameworks/", "pages": []}, {"name": "Swiss Cheese 模型", "path": "HFE_Foundations/swiss_cheese/", "pages": []}], "风险方法": [{"name": "风险方法总览", "path": "HFE_Risk_Methods/", "pages": []}, {"name": "错误分析方法", "path": "HFE_Risk_Methods/error_analysis_methods/", "pages": []}, {"name": "任务分析", "path": "HFE_Risk_Methods/task_analysis/", "pages": []}, {"name": "URRA方法", "path": "HFE_Risk_Methods/urra_methods/", "pages": []}, {"name": "Known Problem 与事件树", "path": "HFE_Risk_Methods/known_problem_and_event_tree/", "pages": []}], "医疗器械": [{"name": "医疗器械总览", "path": "HFE_Medical_Devices/", "pages": []}, {"name": "ISO 14971", "path": "HFE_Medical_Devices/iso_14971/", "pages": []}, {"name": "医疗器械URRA", "path": "HFE_Medical_Devices/medical_device_urra/", "pages": []}, {"name": "医疗器械使用错误", "path": "HFE_Medical_Devices/medical_device_use_errors/", "pages": []}, {"name": "EpiPen工作簿", "path": "HFE_Medical_Devices/epipen_workbook/", "pages": []}], "航空与自动化": [{"name": "航空与自动化总览", "path": "HFE_Aviation_Automation/", "pages": []}, {"name": "航空与自动化导论", "path": "HFE_Aviation_Automation/aviation_automation_intro/", "pages": []}, {"name": "CRM", "path": "HFE_Aviation_Automation/crew_resource_management/", "pages": []}, {"name": "显示与告警", "path": "HFE_Aviation_Automation/displays_and_alerts/", "pages": []}, {"name": "检查单与程序", "path": "HFE_Aviation_Automation/checklists_and_procedures/", "pages": []}, {"name": "自动化车辆", "path": "HFE_Aviation_Automation/automated_vehicles/", "pages": []}], "人的表现": [{"name": "人的表现总览", "path": "HFE_Human_Performance/", "pages": []}, {"name": "注意与监控", "path": "HFE_Human_Performance/attention_and_monitoring/", "pages": []}, {"name": "疲劳与睡眠", "path": "HFE_Human_Performance/fatigue_and_sleep/", "pages": []}, {"name": "压力与决策", "path": "HFE_Human_Performance/stress_and_decision_making/", "pages": []}, {"name": "情境意识", "path": "HFE_Human_Performance/situation_awareness/", "pages": []}, {"name": "空间定向错觉", "path": "HFE_Human_Performance/spatial_disorientation/", "pages": []}], "案例与伦理": [{"name": "案例与伦理总览", "path": "HFE_Cases_Ethics/", "pages": []}, {"name": "Operational Risk", "path": "HFE_Cases_Ethics/operational_risk/", "pages": []}, {"name": "Cardosi案例", "path": "HFE_Cases_Ethics/cardosi_case/", "pages": []}, {"name": "F16分析提示", "path": "HFE_Cases_Ethics/f16_analysis_prompts/", "pages": []}, {"name": "Boeing 737 Max与伦理", "path": "HFE_Cases_Ethics/boeing_737max_and_ethics/", "pages": []}], "HFE Foundations": [{"name": "HFE Foundations Overview", "path": "HFE_Foundations/", "pages": []}, {"name": "Course Overview", "path": "HFE_Foundations/course_overview/", "pages": []}, {"name": "Introduction to Human Factors", "path": "HFE_Foundations/human_factors_intro/", "pages": []}, {"name": "Human Error Frameworks", "path": "HFE_Foundations/human_error_frameworks/", "pages": []}, {"name": "Swiss Cheese Model", "path": "HFE_Foundations/swiss_cheese/", "pages": []}], "Risk Methods": [{"name": "Risk Methods Overview", "path": "HFE_Risk_Methods/", "pages": []}, {"name": "Error Analysis Methods", "path": "HFE_Risk_Methods/error_analysis_methods/", "pages": []}, {"name": "Task Analysis", "path": "HFE_Risk_Methods/task_analysis/", "pages": []}, {"name": "URRA Methods", "path": "HFE_Risk_Methods/urra_methods/", "pages": []}, {"name": "Known Problems and Event Trees", "path": "HFE_Risk_Methods/known_problem_and_event_tree/", "pages": []}], "Medical Devices": [{"name": "Medical Devices Overview", "path": "HFE_Medical_Devices/", "pages": []}, {"name": "ISO 14971", "path": "HFE_Medical_Devices/iso_14971/", "pages": []}, {"name": "Medical Device URRA", "path": "HFE_Medical_Devices/medical_device_urra/", "pages": []}, {"name": "Medical Device Use Errors", "path": "HFE_Medical_Devices/medical_device_use_errors/", "pages": []}, {"name": "EpiPen Workbook", "path": "HFE_Medical_Devices/epipen_workbook/", "pages": []}], "Aviation & Automation": [{"name": "Aviation & Automation Overview", "path": "HFE_Aviation_Automation/", "pages": []}, {"name": "Aviation and Automation Intro", "path": "HFE_Aviation_Automation/aviation_automation_intro/", "pages": []}, {"name": "CRM", "path": "HFE_Aviation_Automation/crew_resource_management/", "pages": []}, {"name": "Displays and Alerts", "path": "HFE_Aviation_Automation/displays_and_alerts/", "pages": []}, {"name": "Checklists and Procedures", "path": "HFE_Aviation_Automation/checklists_and_procedures/", "pages": []}, {"name": "Automated Vehicles", "path": "HFE_Aviation_Automation/automated_vehicles/", "pages": []}], "Human Performance": [{"name": "Human Performance Overview", "path": "HFE_Human_Performance/", "pages": []}, {"name": "Attention and Monitoring", "path": "HFE_Human_Performance/attention_and_monitoring/", "pages": []}, {"name": "Fatigue and Sleep", "path": "HFE_Human_Performance/fatigue_and_sleep/", "pages": []}, {"name": "Stress and Decision Making", "path": "HFE_Human_Performance/stress_and_decision_making/", "pages": []}, {"name": "Situation Awareness", "path": "HFE_Human_Performance/situation_awareness/", "pages": []}, {"name": "Spatial Disorientation", "path": "HFE_Human_Performance/spatial_disorientation/", "pages": []}], "Cases & Ethics": [{"name": "Cases & Ethics Overview", "path": "HFE_Cases_Ethics/", "pages": []}, {"name": "Operational Risk", "path": "HFE_Cases_Ethics/operational_risk/", "pages": []}, {"name": "Cardosi Case", "path": "HFE_Cases_Ethics/cardosi_case/", "pages": []}, {"name": "F16 Analysis Prompts", "path": "HFE_Cases_Ethics/f16_analysis_prompts/", "pages": []}, {"name": "Boeing 737 Max and Ethics", "path": "HFE_Cases_Ethics/boeing_737max_and_ethics/", "pages": []}]};

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
