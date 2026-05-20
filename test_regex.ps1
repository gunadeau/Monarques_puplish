$names = @(
    "TOROS 3 - 9U - B - Masculin - LOTBINIÈRE",
    "MONARQUES BLEU 13UAA",
    "MONARQUES BLEU - 13U - AA",
    "TITANS 5 9UB",
    "JAYS - 13U - A - MASCULIN"
)

$pattern = '^([A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ0-9]+)*?)\s*(?:-)?\s*(\d+U).*?([AB]{1,2})(?![A-Za-z])'

foreach ($name in $names) {
    if ($name -match $pattern) {
        $teamName = $matches[1].Trim()
        $ageGroup = $matches[2]
        $division = $matches[3]
        Write-Host "'$name' -> '$teamName $ageGroup$division'"
    } else {
        Write-Host "'$name' -> NO MATCH"
    }
}
