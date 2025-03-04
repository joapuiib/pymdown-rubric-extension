import markdown
import textwrap

def test_empty_rubric():
    extensions = ['rubric']
    extension_configs = {}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = R'''
    /// rubric
    ///
    '''

    expected_html = R'''
    <table></table>
    '''

    markdown_text = textwrap.dedent(markdown_text).strip()
    expected_html = textwrap.dedent(expected_html).strip()

    html = md.convert(markdown_text)
    assert html == expected_html


def test_basic_rubric():
    extensions = ['rubric']
    extension_configs = {}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = R'''
    /// rubric
    levels:
      - "__Excellent__"
      - "`Good`"
      - "[Acceptable](#acceptable)"
      - Poor

    criteria:
      - title: Clarity
        description: The writing is clear and easy to understand.
        levels:
          - The writing is excellent.
          - The writing is good.
          - The writing is acceptable.
          - The writing is poor.
    ///
    '''

    expected_html = R'''
    <table>
    <thead>
    <tr>
    <th></th>
    <th>
    <div class="rubric__level-title"><strong>Excellent</strong></div>
    </th>
    <th>
    <div class="rubric__level-title"><code>Good</code></div>
    </th>
    <th>
    <div class="rubric__level-title"><a href="#acceptable">Acceptable</a></div>
    </th>
    <th>
    <div class="rubric__level-title">Poor</div>
    </th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    <div class="rubric__criteria-title">Clarity</div>
    <div class="rubric__criteria-description">The writing is clear and easy to understand.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is excellent.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is good.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is acceptable.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is poor.</div>
    </td>
    </tr>
    </tbody>
    </table>
    '''

    markdown_text = textwrap.dedent(markdown_text).strip()
    expected_html = textwrap.dedent(expected_html).strip()

    html = md.convert(markdown_text)
    assert html == expected_html


def test_basic_rubric_with_markdown_content():
    extensions = ['rubric']
    extension_configs = {}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = R'''
    /// rubric
    levels:
      - Exellent
      - Good
      - Acceptable
      - Poor

    criteria:
      - title: Clarity
        description: The writing is __clear__ and easy to understand.
        levels:
          - The writing is __excellent__.
          - The writing is _good_.
          - The writing is [acceptable](#acceptable).
          - The writing is poor.
    ///
    '''

    expected_html = R'''
    <table>
    <thead>
    <tr>
    <th></th>
    <th>
    <div class="rubric__level-title">Exellent</div>
    </th>
    <th>
    <div class="rubric__level-title">Good</div>
    </th>
    <th>
    <div class="rubric__level-title">Acceptable</div>
    </th>
    <th>
    <div class="rubric__level-title">Poor</div>
    </th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    <div class="rubric__criteria-title">Clarity</div>
    <div class="rubric__criteria-description">The writing is <strong>clear</strong> and easy to understand.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is <strong>excellent</strong>.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is <em>good</em>.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is <a href="#acceptable">acceptable</a>.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is poor.</div>
    </td>
    </tr>
    </tbody>
    </table>
    '''

    markdown_text = textwrap.dedent(markdown_text).strip()
    expected_html = textwrap.dedent(expected_html).strip()

    html = md.convert(markdown_text)
    assert html == expected_html

def test_add_classes():
    extensions = ['rubric']
    extension_configs = {'rubric': {'classes': 'my-class'}}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = R'''
    /// rubric
    levels:
      - Excellent

    criteria:
      - title: Clarity
        description: The writing is clear and easy to understand.
        levels:
          - The writing is excellent.
    ///
    '''

    expected_html = R'''
    <table class="my-class">
    <thead>
    <tr>
    <th></th>
    <th>
    <div class="rubric__level-title">Excellent</div>
    </th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    <div class="rubric__criteria-title">Clarity</div>
    <div class="rubric__criteria-description">The writing is clear and easy to understand.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is excellent.</div>
    </td>
    </tr>
    </tbody>
    </table>
    '''

    markdown_text = textwrap.dedent(markdown_text).strip()
    expected_html = textwrap.dedent(expected_html).strip()

    html = md.convert(markdown_text)
    assert html == expected_html


def test_add_classes():
    extensions = ['rubric']
    extension_configs = {'rubric': {'classes': 'my-class'}}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = R'''
    /// rubric
    levels:
      - Excellent

    criteria:
      - title: Clarity
        description: The writing is clear and easy to understand.
        levels:
          - The writing is excellent.
    ///
    '''

    expected_html = R'''
    <table class="my-class">
    <thead>
    <tr>
    <th></th>
    <th>
    <div class="rubric__level-title">Excellent</div>
    </th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    <div class="rubric__criteria-title">Clarity</div>
    <div class="rubric__criteria-description">The writing is clear and easy to understand.</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is excellent.</div>
    </td>
    </tr>
    </tbody>
    </table>
    '''

    markdown_text = textwrap.dedent(markdown_text).strip()
    expected_html = textwrap.dedent(expected_html).strip()

    html = md.convert(markdown_text)
    assert html == expected_html


def test_rubric_with_scores():
    extensions = ['rubric']
    extension_configs = {'rubric': {'classes': 'my-class'}}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = R'''
    /// rubric
    levels:
      - title: Excellent
        score: 4 points
      - Good

    criteria:
      - title: Clarity
        description: The writing is clear and easy to understand.
        score: 4 points
        levels:
          - title: The writing is excellent.
            score: 4 points
          - The writing is good.
    ///
    '''

    expected_html = R'''
    <table class="my-class">
    <thead>
    <tr>
    <th></th>
    <th>
    <div class="rubric__level-title">Excellent</div>
    <div class="rubric__level-score">4 points</div>
    </th>
    <th>
    <div class="rubric__level-title">Good</div>
    </th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    <div class="rubric__criteria-title">Clarity</div>
    <div class="rubric__criteria-description">The writing is clear and easy to understand.</div>
    <div class="rubric__criteria-score">4 points</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is excellent.</div>
    <div class="rubric__criteria-element-score">4 points</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is good.</div>
    </td>
    </tr>
    </tbody>
    </table>
    '''

    markdown_text = textwrap.dedent(markdown_text).strip()
    expected_html = textwrap.dedent(expected_html).strip()

    html = md.convert(markdown_text)
    assert html == expected_html


def test_rubric_criterion_element_checked():
    extensions = ['rubric']
    extension_configs = {'rubric': {'classes': 'my-class'}}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = R'''
    /// rubric
    levels:
      - title: Excellent
        score: 4 points
      - Good

    criteria:
      - title: Clarity
        description: The writing is clear and easy to understand.
        score: 4 points
        levels:
          - title: The writing is excellent.
            score: 4 points
            checked: true
          - The writing is good.
    ///
    '''

    expected_html = R'''
    <table class="my-class">
    <thead>
    <tr>
    <th></th>
    <th>
    <div class="rubric__level-title">Excellent</div>
    <div class="rubric__level-score">4 points</div>
    </th>
    <th>
    <div class="rubric__level-title">Good</div>
    </th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    <div class="rubric__criteria-title">Clarity</div>
    <div class="rubric__criteria-description">The writing is clear and easy to understand.</div>
    <div class="rubric__criteria-score">4 points</div>
    </td>
    <td class="rubric__criteria-element checked">
    <div class="rubric__criteria-element-description">The writing is excellent.</div>
    <div class="rubric__criteria-element-score">4 points</div>
    </td>
    <td class="rubric__criteria-element">
    <div class="rubric__criteria-element-description">The writing is good.</div>
    </td>
    </tr>
    </tbody>
    </table>
    '''

    markdown_text = textwrap.dedent(markdown_text).strip()
    expected_html = textwrap.dedent(expected_html).strip()

    html = md.convert(markdown_text)
    assert html == expected_html
