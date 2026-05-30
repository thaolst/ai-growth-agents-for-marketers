# Case Study 03 - MEU Planning: Tang target voi budget khong tang

## Boi canh

Dau thang, MEU target tang so voi thang truoc nhung budget giu nguyen. Thoi gian con lai trong thang: 20 ngay.

Cach thuong lam: hop team, nghi campaign, roi uoc tinh MEU. Mat 2-3 ngay, ket qua thuong thieu hoac thua target.

## Prompt su dung

MEU Planning Agent (xem 09-meu-planning-agent/prompt.md)

## Quy trinh

Input vao prompt: MEU target, baseline hien tai, budget, so ngay con lai, cac channel dang co, constraint (khong discount sau qua X%).

Agent tra ve trong 30 phut: gap analysis, 3 campaign cu the voi mechanic va budget, MEU du kien tung campaign, confidence level tong, va Plan B neu plan chinh khong du.

## Ket qua thuc te (an danh so lieu)

MEU dat tren 90% target. Campaign thu nhat (dormant reactivation) overperform. Campaign thu hai (frequency booster) underperform do pool nho hon uoc tinh.

Plan B agent de xuat (mo rong sang dormant 60-90 ngay) duoc kích hoat va bu dap shortfall.

## Bai hoc

Gia tri lon nhat khong phai o do chinh xac cua du bao MEU. Ma o viec co san Plan B ro rang truoc khi bat dau. Truoc day khi campaign underperform, mat them 1-2 ngay hop de quyet dinh lam gi tiep theo. Lan nay Plan B da san sang, thuc thi ngay.

# English

## Context

Start of month. MEU target increased vs previous month but budget stayed flat. Days remaining: 20.

Old process: team meeting, brainstorm campaigns, estimate MEU. Took 2-3 days, results often missed or overshot target.

## Real results (anonymized)

MEU reached above 90% of target. First campaign (dormant reactivation) overperformed. Second campaign (frequency booster) underperformed due to pool being smaller than estimated.

Plan B suggested by the agent (expand to 60-90 day dormant users) was activated and covered the shortfall.

## Key lesson

The biggest value was not forecast accuracy. It was having a clear Plan B before starting. Previously when a campaign underperformed, another 1-2 days were lost deciding what to do next. This time Plan B was ready to execute immediately.
