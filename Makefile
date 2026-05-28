.PHONY: setup validate run lint clean

# ── Setup ──────────────────────────────────────────────────────

setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	cp -n .env.example .env 2>/dev/null || echo ".env already exists, skipping"
	@echo "✅ Ready. Edit .env with your API keys."

# ── Validate ───────────────────────────────────────────────────

validate:
	@echo "=== Checking agent directories ==="
	@for dir in 0*/ 10*/; do \
		dir=$${dir%/}; \
		echo -n "  $$dir ... "; \
		missing=""; \
		for file in README.md prompt.md example-output.md; do \
			[ -f "$$dir/$$file" ] || missing="$$missing $$file"; \
		done; \
		if [ -n "$$missing" ]; then \
			echo "❌ Missing:$$missing"; \
			exit 1; \
		fi; \
		echo "✅"; \
	done
	@echo "✅ All agent directories complete"

	@echo "=== Checking Python syntax ==="
	@for f in */*/agent.py; do \
		echo -n "  $$f ... "; \
		python3 -c "import ast; ast.parse(open('$$f').read())" 2>/dev/null && echo "✅" || (echo "❌ Syntax error"; exit 1); \
	done
	@echo "✅ All Python files valid"

	@echo "=== Checking .env.example ==="
	@[ -f .env.example ] && echo "  ✅ Present" || (echo "  ❌ Missing"; exit 1)

	@echo "=== Checking skills ==="
	@for skill in skills/*/; do \
		[ -f "$${skill}SKILL.md" ] && echo "  ✅ $${skill}" || (echo "  ❌ Missing SKILL.md in $${skill}"; exit 1); \
	done

	@echo ""
	@echo "🎉 All checks passed!"

# ── Run an agent ───────────────────────────────────────────────
# Use: make run AGENT=08-ab-test-analyzer

run:
	@if [ -z "$(AGENT)" ]; then \
		echo "Usage: make run AGENT=08-ab-test-analyzer"; \
		echo "Available agents with Python:"; \
		for d in 04 05 07 08 09 10; do \
			path=$$(ls -d $${d}-*/ 2>/dev/null); \
			[ -n "$$path" ] && echo "  - $$path"; \
		done; \
		exit 1; \
	fi
	@if [ ! -f "$(AGENT)/agent.py" ]; then \
		echo "❌ Agent '$(AGENT)' has no agent.py"; \
		exit 1; \
	fi
	@cd "$(AGENT)" && python3 agent.py

# ── List all agents ────────────────────────────────────────────

list:
	@echo "Available agents:"; \
	for d in 0*/ 10*/; do \
		name=$$(echo "$$d" | sed 's/..-//; s:/::'); \
		has_py=""; \
		[ -f "$$d/agent.py" ] && has_py=" 🐍"; \
		echo "  $$d$$has_py"; \
	done

# ── Lint markdown ──────────────────────────────────────────────

lint:
	@which markdownlint 2>/dev/null 1>/dev/null || (echo "Install markdownlint: npm install -g markdownlint-cli"; exit 1)
	markdownlint '**/*.md' --ignore node_modules

# ── Clean ──────────────────────────────────────────────────────

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "✅ Cleaned up"
