/* Academic manager: task tracker + CGPA calculator (5.0 scale). Data saved in this browser. */
(function () {
  'use strict';

  function load(key, fallback) {
    try { var v = JSON.parse(localStorage.getItem(key)); return v == null ? fallback : v; } catch (e) { return fallback; }
  }
  function save(key, val) { try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {} }
  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function today() { var d = new Date(); d.setHours(0, 0, 0, 0); return d; }

  /* ================= Tasks ================= */
  var tasks = load('sp_tasks', []);
  var filter = 'all';
  var list = document.getElementById('task-list');
  var taskForm = document.getElementById('task-form');
  var taskError = document.getElementById('task-error');

  function renderTasks() {
    var shown = tasks.filter(function (t) {
      return filter === 'all' || (filter === 'done' ? t.done : !t.done);
    }).sort(function (a, b) {
      if (a.done !== b.done) return a.done ? 1 : -1;
      return (a.due || '9999').localeCompare(b.due || '9999');
    });

    if (!shown.length) {
      list.innerHTML = '<li class="empty">' + (tasks.length ? 'Nothing here. Try another filter.' : 'No tasks yet. Add your first assignment above.') + '</li>';
    } else {
      list.innerHTML = shown.map(function (t) {
        var overdue = !t.done && t.due && new Date(t.due + 'T00:00:00') < today();
        var meta = [t.course, t.due ? 'Due ' + t.due : 'No due date', t.priority].filter(Boolean).join(' · ');
        return '<li class="task ' + t.priority + (t.done ? ' done' : '') + (overdue ? ' overdue' : '') + '" data-id="' + t.id + '">' +
          '<input type="checkbox" aria-label="Mark ' + esc(t.title) + ' as done"' + (t.done ? ' checked' : '') + '>' +
          '<div><div class="t-title">' + esc(t.title) + '</div><div class="t-meta">' + esc(meta) + (overdue ? ' · Overdue' : '') + '</div></div>' +
          '<button class="icon-btn" aria-label="Delete ' + esc(t.title) + '">✕</button></li>';
      }).join('');
    }

    var done = tasks.filter(function (t) { return t.done; }).length;
    document.getElementById('stat-pending').textContent = tasks.length - done;
    document.getElementById('stat-done').textContent = done;
  }

  if (taskForm) {
    taskForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var title = taskForm.elements.title.value.trim();
      if (title.length < 3) { taskError.textContent = 'Enter a task title of at least 3 characters.'; return; }
      taskError.textContent = '';
      tasks.push({
        id: Date.now(),
        title: title,
        course: taskForm.elements.course.value.trim(),
        due: taskForm.elements.due.value,
        priority: taskForm.elements.priority.value,
        done: false
      });
      save('sp_tasks', tasks);
      taskForm.reset();
      renderTasks();
    });

    list.addEventListener('change', function (e) {
      if (e.target.type !== 'checkbox') return;
      var id = Number(e.target.closest('.task').dataset.id);
      tasks.forEach(function (t) { if (t.id === id) t.done = e.target.checked; });
      save('sp_tasks', tasks); renderTasks();
    });
    list.addEventListener('click', function (e) {
      if (!e.target.classList.contains('icon-btn')) return;
      var id = Number(e.target.closest('.task').dataset.id);
      tasks = tasks.filter(function (t) { return t.id !== id; });
      save('sp_tasks', tasks); renderTasks();
    });
    document.querySelectorAll('.chip[data-task-filter]').forEach(function (chip) {
      chip.addEventListener('click', function () {
        filter = chip.dataset.taskFilter;
        document.querySelectorAll('.chip[data-task-filter]').forEach(function (c) { c.classList.toggle('on', c === chip); });
        renderTasks();
      });
    });
    renderTasks();
  }

  /* ================= CGPA calculator ================= */
  var points = { A: 5, B: 4, C: 3, D: 2, E: 1, F: 0 };
  var body = document.getElementById('gpa-body');
  var courses = load('sp_courses', [{ name: '', units: 3, grade: 'A' }]);

  function rowHtml(c, i) {
    var opts = Object.keys(points).map(function (g) {
      return '<option' + (g === c.grade ? ' selected' : '') + '>' + g + '</option>';
    }).join('');
    return '<tr data-i="' + i + '">' +
      '<td><input type="text" class="c-name" placeholder="e.g. CSC 101" value="' + esc(c.name) + '" aria-label="Course name"></td>' +
      '<td><input type="number" class="c-units" min="1" max="6" value="' + c.units + '" aria-label="Credit units"></td>' +
      '<td><select class="c-grade" aria-label="Grade">' + opts + '</select></td>' +
      '<td><button type="button" class="icon-btn" aria-label="Remove course">✕</button></td></tr>';
  }

  function calc() {
    var units = 0, total = 0;
    courses.forEach(function (c) {
      var u = Number(c.units);
      if (u > 0) { units += u; total += u * points[c.grade]; }
    });
    var gpa = units ? (total / units) : 0;
    document.getElementById('gpa-value').textContent = units ? gpa.toFixed(2) : '–';
    document.getElementById('stat-gpa').textContent = units ? gpa.toFixed(2) : '–';
    document.getElementById('gpa-units').textContent = units + ' credit units counted';
    var cls = '';
    if (units) cls = gpa >= 4.5 ? 'First Class' : gpa >= 3.5 ? 'Second Class Upper' : gpa >= 2.4 ? 'Second Class Lower' : gpa >= 1.5 ? 'Third Class' : 'Pass / Below';
    document.getElementById('gpa-class').textContent = cls;
  }

  function renderCourses() {
    body.innerHTML = courses.map(rowHtml).join('');
    calc();
  }

  if (body) {
    body.addEventListener('input', function (e) {
      var i = Number(e.target.closest('tr').dataset.i);
      if (e.target.classList.contains('c-name')) courses[i].name = e.target.value;
      if (e.target.classList.contains('c-units')) courses[i].units = e.target.value;
      save('sp_courses', courses); calc();
    });
    body.addEventListener('change', function (e) {
      if (!e.target.classList.contains('c-grade')) return;
      courses[Number(e.target.closest('tr').dataset.i)].grade = e.target.value;
      save('sp_courses', courses); calc();
    });
    body.addEventListener('click', function (e) {
      if (!e.target.classList.contains('icon-btn')) return;
      courses.splice(Number(e.target.closest('tr').dataset.i), 1);
      if (!courses.length) courses.push({ name: '', units: 3, grade: 'A' });
      save('sp_courses', courses); renderCourses();
    });
    document.getElementById('add-course').addEventListener('click', function () {
      courses.push({ name: '', units: 3, grade: 'A' });
      save('sp_courses', courses); renderCourses();
    });
    document.getElementById('reset-courses').addEventListener('click', function () {
      courses = [{ name: '', units: 3, grade: 'A' }];
      save('sp_courses', courses); renderCourses();
    });
    renderCourses();
  }
})();
